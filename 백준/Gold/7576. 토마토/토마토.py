import sys
input = sys.stdin.readline
from collections import deque

m, n = map(int, input().split())

tomato = [list(map(int, input().split())) for _ in range(n)] # n X m 토마토 2차원 배열

all_ripe = 1
# 안익은 토마토가 있는지 확인 => 시작할 때
for t in tomato:
    if 0 in t:
        all_ripe = 0
        break # 하나만 있어도 있다는거니까 스탑
    
# 만약 이미 다 익었다면 종료
if all_ripe:
    print(0)
    sys.exit()


dq = deque()
# 익은 토마토 방문 처리
for y in range(n):
    for x in range(m):
        if tomato[y][x] == 1:
            dq.append((x, y, 0)) # 처음 상태 0일


# 방향 벡터
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


max_day = 0 # 걸린 일 수
while dq:
    cx, cy, day = dq.popleft()
    #
    max_day = max(max_day, day)
    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]

        # 경계값 체크
        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            continue
        # 안익은 토마토(0)라면
        if tomato[ny][nx] == 0:
            dq.append((nx, ny, day+1))
            tomato[ny][nx] = 1


for y in range(n):
    for x in range(m):
        if tomato[y][x] == 0:
            print(-1)
            sys.exit()


print(max_day)
