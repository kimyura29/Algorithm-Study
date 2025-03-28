import sys
input = sys.stdin.readline
a = int(input())
b = int(input())
c = int(input())

n = list(str(a * b * c)) # [1, 2, 3, ...]
for i in range(10):
    print(n.count(str(i)))
