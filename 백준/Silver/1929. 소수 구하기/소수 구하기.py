import sys
input = sys.stdin.readline

m, n = map(int, input().split())

result = []

def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True # 소수면 True 반환

for i in range(m, n+1):
    if is_prime(i):
        result.append(i)
for j in result:
    print(j)

