nums = [[3, 1, 2, 1, 3], [], [-1, -1, 0, 2, 2], [1.0, 1, 2.5, 2.5, 0]]


def unique_sorted(nums):
    if not nums:
        return []
    return sorted(set(nums))


for num in nums:
    print(f"{num} -> {unique_sorted(num)}")
