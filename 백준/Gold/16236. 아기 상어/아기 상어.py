import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]

total_time = 0 # 전체 이동 시간
eat_count = 0 # 먹은 물고기 수
shark_size = 2 # 현재 아기상어 크기

# 1. 아기상어 위치 찾기
found = False # flag 변수 사용
for i in range(n):
    for j in range(n):
        if maps[j][i] == 9:
            y, x = j, i # 현재 위치 저장
            maps[j][i] = 0 # 위치 찾았으니까 0으로 표시(물고기랑 헷갈리지 않게)
            found = True
            break
    if found:  # 이미 찾았으면 for문 탈출
        break

# 방향벡터
# 상 하 우 좌
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 2. BFS 탐색
def bfs(x, y):
    queue = deque()
    visit = set()
    # 위치, 거리 저장
    queue.append((x, y, 0)) # 시작점에서 거리 0
    visit.add((x, y))
    eat_fish = []
    while queue:
        cx, cy, d = queue.popleft()
        # 아기상어 상하좌우 탐색 

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            # 1. 방문이 가능한지 -> 경계값 체크(가능한지)  
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            
            # 2. 방문 여부, 이동 가능 여부 (물고기 크기가 아기상어와 작거나 같을 때)
            if (nx, ny) not in visit and maps[ny][nx] <= shark_size:
                queue.append((nx, ny, d+1)) # 거리 + 1
                visit.add((nx, ny))

            # 3. 먹을 수 있는 물고기 후보로 저장
            if 0 < maps[ny][nx] < shark_size:
                eat_fish.append((d+1, ny, nx)) # 우선순위가 거리> y > x 순이니까 

    return eat_fish

# 3. 물고기 탐색 -> 먹기 -> 반복
while True:
    fishes = bfs(x, y) # 현재 위치에서 시작

    if not fishes:  # 더이상 먹을 물고기 없으면
        break 

    fishes.sort() # 물고기 후보 우선순위대로 정렬(거리, 위쪽, 왼쪽)
    dist, ny, nx = fishes[0]

    total_time += dist # 한 칸 이동에 1초
    eat_count += 1
    maps[ny][nx] = 0 # 먹은 물고기 맵에서 제거
    x, y = nx, ny # 상어 위치 이동

    if eat_count == shark_size:
        shark_size += 1
        eat_count = 0

print(total_time)
