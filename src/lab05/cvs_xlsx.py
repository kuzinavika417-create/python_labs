import csv
from pathlib import Path
import openpyxl
from openpyxl.utils import get_column_letter

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """
    Конвертирует CSV в XLSX.
    Использовать openpyxl ИЛИ xlsxwriter.
    Первая строка CSV — заголовок.
    Лист называется "Sheet1".
    Колонки — автоширина по длине текста (не менее 8 символов).
    """
    csv_file = Path(csv_path)
    if not csv_file.exists():
        raise FileNotFoundError(f'CSV файл не найден')
    if not csv_path.lower().endswith('.csv'):
        raise ValueError(f'Файл должен иметь расширение csv')
    try:
        with open(csv_path, 'r', encoding='utf-8') as csv_file:
            line = csv_file.readline()
            if not line.strip():
                raise ValueError('Пустой CSV файл')
            reader = csv.reader(csv_file)
            data = list(reader)
    except UnicodeDecodeError:
        raise ValueError(f'неправильная кодировка (должна быть UTF-8)')
    except csv.Error:
        raise ValueError(f'неправильный формат CSV файла')
    except Exception as ex:
        raise ValueError(f'Ошибка при чтении файла CSV: {ex}')
    
    if len(data) == 0:
        raise ValueError("CSV файл не содержит данных")
    if len(data) < 1:
        raise ValueError("CSV файл не содержит заголовки")
    
    try:
        work = openpyxl.Workbook()
        sheet = work.active
        title = 'Sheet1'
        for row_idx, row_data in enumerate(data, 1):
            for col_idx, cell_value in enumerate(row_data, 1):
                sheet.cell(row=row_idx, column=col_idx, value=cell_value)
        for col_idx in range(1, len(data[0]) + 1):
            column_letter = get_column_letter(col_idx)
            max_length = 8  # минимальная ширина колонок
            for row in sheet[column_letter]:
                if row.value:
                    max_length = max(max_length, len(str(row.value)))
            sheet.column_dimensions[column_letter].width = max_length + 2 # добавление отступов
        work.save(xlsx_path)
    except Exception as ex:
        raise ValueError(f"Ошибка при создании XLSX файла: {ex}")
    
from openpyxl import Workbook
import csv

wb = Workbook()
ws = wb.active
ws.title = "Sheet1"
output_dir = Path("src/data/out")
output_dir.mkdir(parents=True, exist_ok=True)  

with open("src/data/samples/people.csv", encoding="utf-8") as f:
    reader = csv.reader(f)  
    for row in reader:      
        ws.append(row)      

wb.save("src/data/out/people.xlsx")  