import sys
input = sys.stdin.readline
n,m = map(int,input().split())
listen = set()
listen_see = []
for i in range(n):
    listen.add(input().strip())

for j in range(m):
    name = input().strip()
    if name not in listen:
        continue
    else:
        listen_see.append(name)

listen_see.sort()
print(len(listen_see))
for i in listen_see:
    print(i)