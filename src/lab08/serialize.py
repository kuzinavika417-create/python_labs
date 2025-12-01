import json
from typing import List
from models import Student

def students_to_json(students: List[Student], path: str) -> None:
    data = [student.to_dict() for student in students]
    
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def students_from_json(path: str) -> List[Student]:
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        students = []
        for item in data:
            try:
                student = Student.from_dict(item)
                students.append(student)
            except (ValueError, KeyError) as e:
                print(f"Ошибка при загрузке студента: {e}")
                continue
                
        return students
    except FileNotFoundError:
        print(f"Файл {path} не найден")
        return []
    except json.JSONDecodeError:
        print(f"Ошибка декодирования JSON")
        return []

if __name__ == "__main__":
    input_path = "../../data/lab08/students_input.json"
    students = students_from_json(input_path)
    if students:
        print(f"Успешно загружено {len(students)} студентов:\n")
        for i, student in enumerate(students, 1):
            print(f"{i}. {student}")
    else:
        print("Ошибка при загрузке студентов")
        print(f"Файл {input_path} либо не существует, либо не содержит корректные данные")