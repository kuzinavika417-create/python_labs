import csv
from pathlib import Path


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    with open(path, "r", encoding=encoding) as f:
        return f.read()


def write_csv(
    rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None
) -> None:
    if rows and len(set(len(row) for row in rows)) != 1:
        return ValueError

    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if header:
            writer.writerow(header)
        writer.writerows(rows)


if __name__ == "__main__":
    try:
        txt = read_text("src\lab04\data\input.txt")
        print(f"Прочитано: {txt}")
    except FileNotFoundError:
        print("Файл src\lab04\data\input.txt не найден")

    write_csv([("word", "count"), ("test", 3)], "src\lab04\data\input.txt")
    print("файл csv создан!")
