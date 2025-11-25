def count_freq(tokens: list[str]) -> dict[str, int]:
    alf = list(sorted(set(tokens)))
    f = {}
    for i in alf:
        f[i] = tokens.count(i)
    return f


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    sort = sorted(freq.items(), key=lambda i: (-i[1], i[0]))
    return sort[:n]


test = 'Токены ["a","b","a","c","b","a"] → частоты {"a":3,"b":2,"c":1};'
test2 = 'токены ["bb","aa","bb","aa","cc"] → частоты {"aa":2,"bb":2,"cc":1}'
print("тест кейсы для count_freq + top_n")
print(
    f'{repr(test)}; {count_freq(["a","b","a","c","b","a"])} -> {top_n({"a":3,"b":2,"c":1})}'
)
print(
    f'{repr(test2)}; {count_freq(["bb","aa","bb","aa","cc"])} -> {top_n({"aa":2,"bb":2,"cc":1})}'
)
