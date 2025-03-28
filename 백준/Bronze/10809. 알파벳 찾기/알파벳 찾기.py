import sys
input = sys.stdin.readline
n = input().strip()

alpa = 'abcdefghijklmnopqrstuvwxyz'

for a in alpa:
    if a in n:
        print(n.index(a), end=' ') # 공백있게 출력
    else:
        print(-1, end=' ')
