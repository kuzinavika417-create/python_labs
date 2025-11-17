import argparse
import sys
import os
from pathlib import Path
lab06_dir = Path(__file__).parent
project_root = lab06_dir.parent

if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

pythonpath = os.environ.get('PYTHONPATH', '')
if str(project_root) not in pythonpath.split(os.pathsep):
    os.environ['PYTHONPATH'] = str(project_root) + (os.pathsep + pythonpath if pythonpath else '')

from lib.text import normalize, tokenize, count_freq, top_n

def cmd_cat(input_path: str, number_lines: bool = False) -> None:
    normalized_path = input_path.replace('\\', '/')
    if normalized_path.startswith('src/'):
        normalized_path = normalized_path[4:]
    
    input_file = Path(normalized_path)
    
    # Если файл не найден, проверка относительно src
    if not input_file.exists():
        src_path = project_root / normalized_path
        if src_path.exists():
            input_file = src_path
        else:
            raise FileNotFoundError(f"Файл не найден: {input_path}")
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, start=1):
                if number_lines:
                    print(f"{line_num:6d}\t{line}", end='')
                else:
                    print(line, end='')
    except Exception as e:
        raise IOError(f"Ошибка чтения файла {input_file}: {e}")

def cmd_stats(input_path: str, top: int = 5) -> None:
    normalized_path = input_path.replace('\\', '/')
    if normalized_path.startswith('src/'):
        normalized_path = normalized_path[4:]
    
    input_file = Path(normalized_path)
    
    # Если файл не найден, проверка относительно src
    if not input_file.exists():
        src_path = project_root / normalized_path
        if src_path.exists():
            input_file = src_path
        else:
            raise FileNotFoundError(f"Файл не найден: {input_path}")
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            text = f.read()
    except Exception as e:
        raise IOError(f"Ошибка чтения файла {input_file}: {e}")
    
    if not text.strip():
        print("Файл пустой", file=sys.stderr)
        return
    
    # Обработка текста
    normalized = normalize(text)
    tokens = tokenize(normalized)
    
    if not tokens:
        print("После обработки слов не найдено", file=sys.stderr)
        return
    
    # Подсчет частот
    freq = count_freq(tokens)
    top_words = top_n(freq, n=top)
    
    # Вывод результатов
    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print(f"Топ-{top}:")
    for word, count in top_words:
        print(f"  {word}: {count}")


def main():
    parser = argparse.ArgumentParser(description="CLI-утилиты для работы с текстом (cat/stats)")
    parser.add_argument("--input",required=True,help="Путь к входному файлу")
    parser.add_argument("-n",action="store_true",help="Нумеровать строки (для команды cat)")
    parser.add_argument("--top",type=int,default=None,help="Количество топ-слов для вывода (если указан, выполняется stats)")
    
    args = parser.parse_args()
    
    try:
        if args.top is not None:
            if args.top < 1:
                parser.error("--top должен быть положительным числом")
            cmd_stats(args.input, args.top)
        else:
            cmd_cat(args.input, args.n)
    except FileNotFoundError as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
