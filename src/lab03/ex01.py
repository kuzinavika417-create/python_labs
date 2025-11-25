def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if not text:
        return ""
    for i in "\t\r\n\v\f":
        text = text.replace(i, " ")
    while "  " in text:
        text = text.replace("  ", " ")
    text = text.strip()
    if yo2e:
        text = text.replace("ё", "е").replace("Ё", "Е")
    if casefold:
        text.casefold()
    return text


def tokenize(text: str) -> list[str]:
    text = normalize(text, casefold=False, yo2e=False)
    words = []
    results = []
    for i in text:
        if i.isalnum() or i == "_" or i == "-" in words:
            words.append(i)
        elif words:
            results.append("".join(words))
            words = []
    if words:
        results.append("".join(words))
    return results


test_normalize = "ПрИвЕт\nМИр\t"
test1_normalize = "ёжик, Ёлка"
test2_normalize = "Hello\r\nWorld"
test3_normalize = "  двойные   пробелы  "
test_tokenize = "привет мир"
test2_tokenize = "hello,world!!!"
test3_tokenize = "по-настоящему круто"
test4_tokenize = "2025 год"
test5_tokenize = "emoji 😀 не слово"
print("тест кейсы для normalize:")
print(f"{repr(test_normalize)}, {repr(normalize(test_normalize).casefold())}")
print(f"{repr(test1_normalize)}, {normalize(test1_normalize)}")
print(f"{repr(test2_normalize)}, {normalize(test2_normalize)}")
print(f"{repr(test3_normalize)}, {normalize(test3_normalize)}")

print("тест кейсы для tokenize")
print(f"{repr(test_tokenize)}, {repr(tokenize(test_tokenize))}")
print(f"{repr(test2_tokenize)}, {repr(tokenize(test2_tokenize))}")
print(f"{repr(test3_tokenize)}, {repr(tokenize(test3_tokenize))}")
print(f"{repr(test4_tokenize)}, {repr(tokenize(test4_tokenize))}")
print(f"{repr(test5_tokenize)}, {repr(tokenize(test5_tokenize))}")
