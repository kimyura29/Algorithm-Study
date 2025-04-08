import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
count = 0
for num in nums:
    is_prime = True
    if num == 1: # 1은 소수가 아니야
        is_prime = False
    
    for i in range(2, int(num ** 0.5)+1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        count += 1
print(count)