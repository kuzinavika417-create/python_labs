import csv
from pathlib import Path
from lab08.models import Student
from datetime import date
import re

class Group:
    def __init__(self, storage_path: str):
        self.path = Path(storage_path)
        if not self.path.exists():
            self.path.write_text("", encoding="utf-8") 
    def _read_all(self):
        rows = []
        try:
            with open(self.path, 'r', newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    rows.append(dict(row))
        except FileNotFoundError:
            with open(self.path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(["fio", "birthdate", "group", "gpa"])
        except Exception as e:
            print(f"Ошибка при чтении CSV файла: {e}")
        
        return rows  # реализовано чтение строк из csv 
    
    def _ensure_storage_exists(self, students: list): # Создать файл с заголовком, если его не существует
        with open(self.path, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["fio", "birthdate", "group", "gpa"])
            writer.writeheader()
            writer.writerows(students)
            
    def list(self):
        rows = self._read_all()
        students = []
        for row in rows:
            try:
                # Преобразование строки CSV в объект Student
                row["gpa"] = float(row["gpa"])
                student = Student.from_dict(row)
                students.append(student)
            except (KeyError, ValueError) as e:
                print(f"Ошибка при создании Student из {row}: {e}")
        return students
          # реализован метод list() - получить всех студентов

    def add(self, student: Student):
        rows = self._read_all()
        for row in rows:
            if row["fio"] == student.fio:
                print(f"Студент с ФИО '{student.fio}' уже существует")
                return
        with open(self.path, 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([
                student.fio,
                student.birthdate,
                student.group,
                str(student.gpa)
            ])
        print(f"Студент {student.fio} успешно добавлен")
         # реализован метод add() - добавление студента

    def find(self, substr: str):
        rows = self._read_all()
        found_rows = [r for r in rows if substr in r["fio"]] # поиск строки CSV, где в поле fio содержится подстрока
        
        # преобразование найденных строк CSV в объекты Student
        found_students = []
        for row in found_rows:
            try:
                student = Student(
                    fio=row["fio"],
                    birthdate=row["birthdate"],
                    group=row["group"],
                    gpa=float(row["gpa"])
                )
                found_students.append(student)
            except (KeyError, ValueError) as e:
                print(f"Ошибка при создании Student из {row}: {e}")
        return found_students
        #  реализован метод find() -  поиск по подстроке в ФИО  

    def remove(self, fio: str):
        rows = self._read_all()
        found = False
        for i, r in enumerate(rows):
            if r["fio"] == fio:
                rows.pop(i)
                found = True
                break
        if not found:
            print(f"Студент с ФИО '{fio}' не найден")
            return
        with open(self.path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["fio", "birthdate", "group", "gpa"])
            writer.writeheader()
            writer.writerows(rows)
        print(f"Студент '{fio}' успешно удален")
        #  реализован метод remove() - удаление по ФИО
        
    def update(self, fio: str, **fields):
        rows = self._read_all()
        found = False
        for row in rows:
            if row["fio"] == fio:
                # обновление указанных полей в строке CSV
                for key, value in fields.items():
                    if key in ["fio", "birthdate", "group", "gpa"]:
                        row[key] = str(value) if key == "gpa" else value
                found = True
                break
        if not found:
            print(f"Студент с ФИО '{fio}' не найден")
            return
        # запись обновленных данных обратно в CSV
        with open(self.path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["fio", "birthdate", "group", "gpa"])
            writer.writeheader()
            writer.writerows(rows)
        print(f"Данные студента '{fio}' успешно обновлены")
        # реализован метод update() - обновление полей существующей записи
    def stats(self):
        students = self._read_all()

        groups = [i["group"] for i in students]
        gpas = [float(student["gpa"]) for student in students]
        group = {group: groups.count(group) for group in set(groups)}
        top_5 = sorted(students, key=lambda s: s["gpa"], reverse=True)[:5]
        top_5_list = [{"fio": s["fio"], "gpa": s["gpa"]} for s in top_5]

        return {
            "count": len(students),
            "min_gpa": self.find_min(gpas),
            "max_gpa": self.find_max(gpas),
            "avg_gpa": sum(gpas) / len(students),
            "groups": group,
            "top_5": top_5_list,
        }
    @staticmethod
    def find_max(array):
        m = -float("inf")
        for i in range(len(array)):
            if array[i] > m:
                m = array[i]
        return m

    @staticmethod
    def find_min(array):
        m = float("inf")
        for i in range(len(array)):
            if array[i] < m:
                m = array[i]
        return m
if __name__ == "__main__":
    group = Group("data/students.csv")
    from lab08.models import Student
    
    student1 = Student(  
        fio="Иванов Иван Иванович",
        birthdate="2000-05-15",
        group="ИТ-101",
        gpa=4.5
    )
    
    # добавление студента через add()
    group.add(student1)
    
    # все сдуденты:
    all_students = group.list()
    print(f"Всего студентов: {len(all_students)}")
    
    # статистика:
    stats = group.stats()
    print(f"\nСтатистика:")
    print(f"  Всего студентов: {stats['count']}")
    print(f"  Средний GPA: {stats['avg_gpa']:.2f}")
    print(f"  Минимальный GPA: {stats['min_gpa']}")
    print(f"  Максимальный GPA: {stats['max_gpa']}")
    print(f"  Распределение по группам: {stats['groups']}")
    print(f"  Топ-5 студентов: {stats['top_5']}")