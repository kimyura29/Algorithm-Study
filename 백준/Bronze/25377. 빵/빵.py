import sys
input = sys.stdin.readline
N = int(input())
min_time = 1001

for _ in range(N):
    A, B = map(int, sys.stdin.readline().split())

    if A <= B and B < min_time:
        min_time = B

if min_time == 1001:
    print(-1)
else:
    print(min_time)