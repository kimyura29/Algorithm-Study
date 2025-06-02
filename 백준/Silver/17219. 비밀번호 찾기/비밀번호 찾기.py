import sys
from collections import defaultdict
input = sys.stdin.readline
n, m  = map(int,input().split())
password = defaultdict(int)
for _ in range(n):
    a, b = input().split()
    password[a] = b
search = []
for _ in range(m):
    search.append(input().strip())

for i in search:
    print(password[i]) 
