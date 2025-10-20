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

def tokenize(text: str) -> list[str]:
    text = normalize(text, casefold=False, yo2e=False)
    words = []
    results = []
    for i in text:
        if i.isalnum() or i == '_' or i == '-' in words:
            words.append(i)
        elif words:
            results.append(''.join(words))
            words = []
    if words:
        results.append(''.join(words))
    return results

def count_freq(tokens: list[str]) -> dict[str, int]:
    alf = list(sorted(set(tokens)))
    f = {}
    for i in alf:
        f[i] = tokens.count(i)
    return f

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    sort = sorted(freq.items(), key=lambda i: (-i[1], i[0]))
    return sort[:n]
