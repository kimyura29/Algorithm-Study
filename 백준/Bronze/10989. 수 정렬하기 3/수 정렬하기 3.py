import sys
input = sys.stdin.readline

n = int(input())
count = [0] * 10001  # 숫자 범위는 1~10000

for _ in range(n):
    num = int(input())
    count[num] += 1

for i in range(1, 10001):
    if count[i] > 0:
        for _ in range(count[i]):
            print(i)