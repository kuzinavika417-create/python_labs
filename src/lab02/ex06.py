def col_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return [] 
    rectangular_matrix = [len(row) for row in mat]
    if len(set(rectangular_matrix)) != 1:
        return 'ValueError'
    A = len(mat[0])
    summa = []
    for i in range(A):
        i_summa = sum(row[i] for row in mat)
        summa.append(i_summa)
    return summa
print(col_sums([[1, 2, 3], [4, 5, 6]]))  
print(col_sums([[-1, 1], [10, -10]]))  
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]])) 