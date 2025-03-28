import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    s = input().strip()
    score = 0
    total = 0

    for i in s:
        if i =='O':
            score += 1
            total += score
        else:
            score = 0
    print(total)
