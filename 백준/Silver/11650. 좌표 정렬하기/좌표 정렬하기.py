import sys
input = sys.stdin.readline

n = int(input())

coordinate = []
for _ in range(n):
    x, y = map(int, input().split())
    coordinate.append((x, y))

coordinate.sort(key = lambda k:(k[0],k[1]))
for x, y in coordinate:
    print(x, y)