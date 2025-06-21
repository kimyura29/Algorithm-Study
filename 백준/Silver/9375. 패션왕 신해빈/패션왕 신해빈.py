import sys
from collections import defaultdict
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input()) # 옷 개수
    clothes = defaultdict(list)
    for _ in range(n):
        a, b = map(str, input().split())
        clothes[b].append(a)
    cnt = 1
    for i in clothes:
        cnt *= (len(clothes[i]) + 1)
    print(cnt-1) # 아무것도 선택 안하는 경우 하나 빼기