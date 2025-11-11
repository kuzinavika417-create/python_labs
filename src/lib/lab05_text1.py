import json
import csv
from pathlib import Path

def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок — алфавитный.
    """
    json_file = Path(json_path)
    with open(json_path, 'r', encoding='utf-8') as json_file : # кодировка UTF-8
        data = json.load(json_file)
    if not json_file.exists():
        raise FileNotFoundError(f"JSON файл отсутствует")
    if not isinstance(data,list):
        raise ValueError('Неверный тип данных')
    if len(data) == 0:
        raise ValueError('Пустой файл JSON')
    all = set()
    for i in data:
        if not isinstance(i,dict):
            raise ValueError('Элементы должны быть словарями')
        all.add(i.keys)
    col = sorted(all)
    
    try:
        with open(csv_path, 'w', encoding='utf-8', newline='') as csv_file:
            csv_file = csv.DictWriter(csv_file, fieldnames=col)
            csv_file.writeheader()
            for i in data:
                row = {r: i.get(r,'') for r in col}
                csv_file.writerow(row)
    except Exception as ex:
        raise ValueError(f'Ошибка при записи CSV: {ex}')
    
def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON (список словарей).
    Заголовок обязателен, значения сохраняются как строки.
    json.dump(..., ensure_ascii=False, indent=2)
    """
    csv_file = Path(csv_path)
    if not csv_file.exists():
        raise FileNotFoundError(f'Файл CSV не найден')
    with open(csv_path, 'r', encoding = 'utf-8') as csv_file:
        line = csv_file.readline()
        if not csv_file.strip():
            raise FileNotFoundError(f'Файл CSV пустой')
        reader = csv.DictReader(csv_file)
        if reader.fieldnames == None:
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
            json.dump(data, json_file, ensure_ascii=False, indent=2) #запись данных в JSON формат (data =данные, json_file = файл куда идет запись
            #ensure_ascii=False - разрешение русских букв (без \u0430\u0431), indent=2 - красивое форматирование с отступами )
    except Exception as ex:
        raise ValueError(f'Ошибка при записи JSON')
    
