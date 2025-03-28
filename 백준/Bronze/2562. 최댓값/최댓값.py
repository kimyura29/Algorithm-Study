import sys
input = sys.stdin.readline

nums= []
for _ in range(9):
    nums.append(int(input().strip())) 

print(max(nums))
print(nums.index(max(nums)) + 1)