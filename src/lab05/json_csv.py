import json
import csv
from pathlib import Path

def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок — алфавитный.
    """
    json_file_path = Path(json_path)
    if not json_file_path.exists():
        raise FileNotFoundError(f"JSON файл отсутствует: {json_path}")
    
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    if not isinstance(data, list):
        raise ValueError('Неверный тип данных')
    if len(data) == 0:
        raise ValueError('Пустой файл JSON')
    
    all_keys = set()
    for i in data:
        if not isinstance(i, dict):
            raise ValueError('Элементы должны быть словарями')
        all_keys.update(i.keys())
    
    col = sorted(all_keys)
    
    try:
        with open(csv_path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=col)
            writer.writeheader()
            for i in data:
                row = {r: i.get(r, '') for r in col}
                writer.writerow(row)
    except Exception as ex:
        raise ValueError(f'Ошибка при записи CSV: {ex}')
    
def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON (список словарей).
    Заголовок обязателен, значения сохраняются как строки.
    json.dump(..., ensure_ascii=False, indent=2)
    """
    csv_file_path = Path(csv_path)
    if not csv_file_path.exists():
        raise FileNotFoundError(f'Файл CSV не найден: {csv_path}')
    
    with open(csv_path, 'r', encoding='utf-8') as f:
        first_line = f.readline()
        if not first_line.strip():
            raise FileNotFoundError(f'Файл CSV пустой: {csv_path}')
        f.seek(0)  # Возвращаемся в начало файла
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            raise ValueError(f'Файл CSV не содержит заголовков')
        
        data = []
        for row in reader:
            string_row = {}
            for key, value in row.items():
                string_row[key] = str(value)
            data.append(string_row)
            
        if len(data) == 0:
            raise ValueError(f'CSV файл не содержит данных, имеет только заголовки')
    
    # запись JSON
    try:
        with open(json_path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=2)
    except Exception as ex:
        raise ValueError(f'Ошибка при записи JSON: {ex}')
    

# data = [{"name": "Alice", "age": 22}, {"name": "Bob", "age": 25}]
# path = Path("src.data/out/people.json")
# path.parent.mkdir(parents=True, exist_ok=True)

# with path.open("w", encoding="utf-8") as f:
#     json.dump(data, f, ensure_ascii=False, indent=2)

# with path.open(encoding="utf-8") as f:
#     loaded_data = json.load(f)
# print(loaded_data)

# rows = [
#     {"name": "Alice", "age": "22", "city": "SPB"},
#     {"name": "Bob", "age": "25", "city": "Moscow"}
# ]
# with open("src.data/out/people.csv", "w", newline="", encoding="utf-8") as f:
#     writer = csv.DictWriter(f, fieldnames=["name", "age", "city"])  
#     writer.writeheader()  
#     writer.writerows(rows)  
# with open("src.data/out/people.csv", encoding="utf-8") as f:
#     reader = csv.DictReader(f)  
#     for row in reader:
#         print(row)