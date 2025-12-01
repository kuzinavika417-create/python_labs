# Лабораторная работа 8
## Задание А
**код:**
``` 
from dataclasses import dataclass
from datetime import datetime, date
import re

@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):
        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d")
        except ValueError:
            raise ValueError(f"Invalid date format: {self.birthdate}. Expected YYYY-MM-DD")
        
        if not (0 <= self.gpa <= 5):
            raise ValueError("gpa must be between 0 and 5")
        
        if not re.match(r'^[A-Za-zА-Яа-яЁё\s\-]+$', self.fio):
            raise ValueError("FIO should contain only letters, spaces and hyphens") #доп валидация ФИО

    def age(self) -> int:
        try:
            birth_date = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError(f"Invalid date format for age calculation: {self.birthdate}")
        
        today = date.today()
        age = today.year - birth_date.year
        
        if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
            age -= 1 # если ДР еще не наступил
        return age

    def to_dict(self) -> dict:
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa
        }

    @classmethod
    def from_dict(cls, d: dict):
        required_fields = ["fio", "birthdate", "group", "gpa"]
        
        for field in required_fields:
            if field not in d:
                raise ValueError(f"Missing required field: {field}")
        
        return cls(
            fio=d["fio"],
            birthdate=d["birthdate"],
            group=d["group"],
            gpa=d["gpa"]
        )

    def __str__(self):
        return f"Student: {self.fio}, Group: {self.group}, GPA: {self.gpa}, Age: {self.age()}"
    
# простой тест
if __name__ == "__main__":
    student = Student(
        fio="Тестовый Студент Николай",
        birthdate="2000-01-01", 
        group="TEST-01",
        gpa=4.5
    )
    print(student)

```
Для работы этого кода необходимо в терминале прописать команду : ``` python src/lab08/models.py ```

Результат кода: 
![alt text](image-1.png)

## Задание В
**код:**
```
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
```
Для работы этого кода необходимо в терминале прописать команду : ``` python src/lab08/serialize.py ```

Результат кода: 
![alt text](image.png)