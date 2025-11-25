def transpose(mat: list[list[float | int]]) -> list[list]:
    if not mat:
        return []
    for i in mat:
        if len(i) != len(mat[0]):
            return "ValueError"
    str = []
    for i in range(len(mat[0])):
        A = []
        for j in range(len(mat)):
            A.append(mat[j][i])
        str.append(A)
    return str


print(f"{[1, 2, 3]} -> {transpose([[1, 2, 3]])}")
print(f"{[1], [2], [3]} -> {transpose([[1], [2], [3]])}")
print(f"{[[1, 2], [3, 4]]} -> {transpose([[1, 2], [3, 4]])}")
print(f"{[]} -> {transpose([])}")
print(f"{[[1, 2], [3]]} -> {transpose([[1, 2], [3]])}")
