import sys
input = sys.stdin.readline

nums = [int(input()) for _ in range(10)]
remain = set() # 중복제거하게

for n in nums:
    remain.add(n%42)

print(len(remain))