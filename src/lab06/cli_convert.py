import argparse
import sys
import os
from pathlib import Path
from lab05.json_csv import json_to_csv, csv_to_json
from lab05.cvs_xlsx import csv_to_xlsx


lab06_dir = Path(__file__).parent
project_root = lab06_dir.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

pythonpath = os.environ.get('PYTHONPATH', '')
if str(project_root) not in pythonpath.split(os.pathsep):
    os.environ['PYTHONPATH'] = str(project_root) + (os.pathsep + pythonpath if pythonpath else '')

def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных (JSON/CSV/XLSX)")
    parser.add_argument("--in",dest="input",required=True,help="Путь к входному файлу")
    parser.add_argument("--out",dest="output",required=True,help="Путь к выходному файлу")
    
    args = parser.parse_args()
    def normalize_path(path: str) -> str:
        normalized = path.replace('\\', '/')
        if normalized.startswith('src/'):
            normalized = normalized[4:]
        return normalized
    
    input_path_str = normalize_path(args.input)
    output_path_str = normalize_path(args.output)
    input_path = Path(input_path_str)
    output_path = Path(output_path_str)
    
    # Если входной файл не найден, пробуем относительно src
    if not input_path.exists() and not input_path.is_absolute():
        src_input_path = project_root / input_path_str
        if src_input_path.exists():
            input_path_str = str(src_input_path)
            input_path = src_input_path
    
    # Для выходного файла создаем путь относительно src, если путь не абсолютный
    if not output_path.is_absolute():
        src_output_path = project_root / output_path_str
        output_path = src_output_path
    
    # Определяем формат по расширениям
    input_ext = input_path.suffix.lower()
    output_ext = output_path.suffix.lower()
    
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    try:
        if input_ext == '.json' and output_ext == '.csv':
            json_to_csv(input_path_str, str(output_path))
        elif input_ext == '.csv' and output_ext == '.json':
            csv_to_json(input_path_str, str(output_path))
        elif input_ext == '.csv' and output_ext == '.xlsx':
            csv_to_xlsx(input_path_str, str(output_path))
        else:
            parser.error(f"Неподдерживаемая конвертация: {input_ext} -> {output_ext}")
        
        print(f"Успешно: {args.input} -> {args.output}")
    except FileNotFoundError as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
