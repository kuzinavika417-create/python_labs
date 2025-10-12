nums = [[[1, 2], [3, 4]],([1, 2], (3, 4, 5)),[[1], [], [2, 3]],[[1, 2], "ab"]]
def flatten(nums):
    r = []
    for i  in nums:
        if type(i) != str:
            for j in i :
                r.append(j)
        else:
            return 'TypeError'
    return r
for i in nums:
     print(f'{i} -> {flatten(i)}')