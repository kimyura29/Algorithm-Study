import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

dq = deque()
visit = set()

# 위치, 시간 
dq.append((n,0))
visit.add(n)

ans = 0
while dq:
    # 현재 위치, 시간
    cx, ct = dq.popleft()

    if cx == k:
        ans = ct
        break

    if cx > 100000:
        continue

    # N+1, N-1, N*2
    #1. 방문이 가능한지 -> 경계값 체크(가능한지)
    #2. 중복체크(방문한적이 있는지)
    
    # 방문 가능 체크 X
    # 중복 체크 -> 없으면 반복

    nx = cx+1
    if nx not in visit:
        # 새로운 지점, 시간+1
        dq.append((nx, ct+1))
        visit.add(nx)

    nx = cx-1
    if nx not in visit:
        # 새로운 지점, 시간+1
        dq.append((nx, ct+1))
        visit.add(nx)

    nx = cx*2
    if nx not in visit:
        # 새로운 지점, 시간+1
        dq.append((nx, ct+1))
        visit.add(nx)

print(ct)
