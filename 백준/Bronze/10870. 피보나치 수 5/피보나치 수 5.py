import sys
input = sys.stdin.readline
n = int(input())

def sol(n):
    if n == 0:
        return 0
    fibo = [0] * (n+1)
    fibo[1] = 1
    for i in range(2, n+1):
        fibo[i] = fibo[i-1] + fibo[i-2]
    return fibo[n]

print(sol(n))
