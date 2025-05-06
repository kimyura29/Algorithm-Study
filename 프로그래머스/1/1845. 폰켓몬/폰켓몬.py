def solution(nums):
    n = len(nums)
    new_n = len(set(nums))
    if new_n >= n // 2:
        return n // 2
    else:
        return new_n