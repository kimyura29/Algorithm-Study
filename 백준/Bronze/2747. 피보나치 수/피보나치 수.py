import sys
input = sys.stdin.readline
n = int(input())

f = [0] * (max(2, n+1)) # n=0 or 1일 때도 최소 크기 2 확보
f[0] = 0
f[1] = 1

for i in range(2, n+1):
    f[i] = f[i-1] + f[i-2]
print(f[n])