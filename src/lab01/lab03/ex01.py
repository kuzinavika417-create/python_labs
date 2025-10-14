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

test = "ПрИвЕт\nМИр\t"
test1 = "ёжик, Ёлка"
test2 = "Hello\r\nWorld"
test3 = "  двойные   пробелы  "
print(f"{repr(test)}, {repr(normalize(test).casefold())}")
print(f'{repr(test1)}, {normalize(test1)}')
print(f'{repr(test2)}, {normalize(test2)}')
print(f'{repr(test3)}, {normalize(test3)}')