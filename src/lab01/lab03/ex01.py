def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if not text:
        return ''
    for i in '\t\r\n\v\f':
        text = text.replace(i,' ')
    while '  ' in text:
        text = text.replace('  ', ' ')
    text = text.strip()
    if yo2e:
        text = text.replace('ё', 'е').replace('Ё', 'Е')
    if casefold:
        text.casefold()
    return text
print('"ПрИвЕт\nМИр\t"', normalize("ПрИвЕт\nМИр\t").casefold())
print('"ёжик, Ёлка"', normalize("ёжик, Ёлка"))
print('"Hello\r\nWorld"', normalize("Hello\r\nWorld"))
print('"  двойные   пробелы  "', normalize("  двойные   пробелы  "))