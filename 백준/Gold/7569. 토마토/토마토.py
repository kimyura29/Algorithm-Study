import sys
from collections import deque
input = sys.stdin.readline

m, n, h = map(int, input().split())

all_ripe = 1 # 모두 익었는지 확인
# 3차원 토마토 입력 받기
tomato = []
for _ in range(h):
    # floor = [list(map(int, input().split())) for _ in range(n)]
    floor = []
    for _ in range(n):
        temp = list(map(int, input().split()))
        # 안 익은 토마토(0)가 있다면
        if 0 in temp:
            all_ripe = 0
        floor.append(temp)
    tomato.append(floor)
# 만약 다 익어있어(0이 없으면) 0 출력
if all_ripe:
    print(0)
    sys.exit()  # 프로그램 종료

# 방향 벡터 설정 (3차원)
dx = [0, 0, 1, -1, 0, 0] 
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

# 방문 여부 확인 => 필요없어
# visit = set()


dq = deque()
# 익은 토마토(=1)인 지점 넣고 시작
for z in range(h): # 높이
    for y in range(n): # 행(y)
        for x in range(m): # 열(x)
            # 토마토가 익었다면
            if tomato[z][y][x] == 1:
                dq.append((x, y, z, 0))
                # visit.add((x, y, z))


max_day = 0 # 처음 0일
while dq:
    cx, cy, cz, day = dq.popleft() # day: 현재 좌표가 익은 날짜
    # 지금 도달한 날짜 중 가장 큰 값 저장 =가장 나중에 익은 토마토까지 퍼지는 데 걸린 시간
    max_day = max(max_day, day)

    for i in range(6):
        nx = cx + dx[i]
        ny = cy + dy[i]
        nz = cz + dz[i]

        # 경계값 체크
        if nx < 0 or nx >= m or ny < 0 or ny >=n or nz < 0 or nz >= h:
            continue
        # 중복 확인, 익은 토마토(1) 주변으로 안익은 토마토(0)가 있는지
        if tomato[nz][ny][nx] == 0:
            dq.append((nx, ny, nz, day+1))
            tomato[nz][ny][nx] = 1 # 0 ->  1로 바뀜(같이 익어)
            # 빈칸(-1)이라면 패스됨
            

# bfs가 다 돌고나서
# 모든 토마토가 익지 못하는 상황(몇 일을 돌아도 0이 사라질 수 없는 상황)이면 -1 출력
for z in range(h): # 높이
    for y in range(n): # 행(y)
        for x in range(m): # 열(x)
            # 토마토가 익지 않은게 남아 있다면
            if tomato[z][y][x] == 0:
                print(-1)
                sys.exit() # 프로그램 종료


# 이렇게 0이 없어질 때까지 다 돌수 있으면 몇일 걸리는지 출력 => 최소일수
print(max_day)
