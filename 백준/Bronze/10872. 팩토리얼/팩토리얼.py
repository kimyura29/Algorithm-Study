import sys
input = sys.stdin.readline
n = int(input())

def sol(n):
    factorial = [1]*(n+1)
    for i in range(n+1):
        if i <= 1:
            factorial[i] = 1
        elif i > 1:
            factorial[i] = factorial[i-1] * i
    
    return factorial[n]

print(sol(n))