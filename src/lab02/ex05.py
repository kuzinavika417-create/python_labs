def row_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []
    rectangular_matrix = [len(row) for row in mat]
    if len(set(rectangular_matrix)) != 1:
        return "ValueError"
    summa = []
    for row in mat:
        row_sum = sum(row)
        summa.append(row_sum)
    return summa


print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
print(row_sums([[1, 2], [3]]))
