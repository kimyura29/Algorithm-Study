import sys
input = sys.stdin.readline
n = int(input())

# t(n) = t(n-1) + 2*t(n-2)

t = [0] * (max(3, n+1))
t[1] = 1
t[2] = 3
for i in range(3, n+1):
    t[i] = t[i-1] + 2 * t[i-2]
print(t[n] % 10007)