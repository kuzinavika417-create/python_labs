nums = [[[1, 2], [3, 4]], ([1, 2], (3, 4, 5)), [[1], [], [2, 3]], [[1, 2], "ab"]]


def flatten(nums):
    exit_material = []
    for i in nums:
        if type(i) != str:
            for j in i:
                exit_material.append(j)
        else:
            return "TypeError"
    return exit_material


for i in nums:
    print(f"{i} -> {flatten(i)}")
