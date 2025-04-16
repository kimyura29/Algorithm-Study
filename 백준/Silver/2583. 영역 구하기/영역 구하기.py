import sys
from collections import deque
input = sys.stdin.readline

m, n, k = map(int,input().split())
maps = [[0]*n for _ in range(m)] # n X m 2차원 배열 만들기
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())

    # # (x1, y1)부터 (x2-1, y2-1)까지 1로 채움 (직사각형 내부 영역)
    for x in range(x1, x2):
        for y in range(y1, y2):
            maps[y][x] = 1 # y는 행, x는 열

# 방문여부
visit = set()

# 방향 벡터 설정(상 하 우 좌)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x,y):
    queue = deque()
    queue.append((x, y)) # 시작점 삽입
    visit.add((x,y)) # 시작점 방문처리
    count = 1 # 현재 영역 넓이 초기화

    # 큐가 빌때까지 반복
    while queue:
        cx, cy = queue.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            
            # 1. 방문이 가능한지 
            if nx < 0 or nx >= n or ny <0 or ny >= m:
                continue

            # 2. 중복 체크 (방문한적이 있는지)
            if (nx, ny) not in visit and maps[ny][nx] == 0:
                queue.append((nx,ny)) # 큐에 추가
                visit.add((nx, ny)) # 방문 처리
                count += 1 # 넓이 + 1
    return count # 해당 영역 넓이 반환

# 각 영역의 넓이 저장
results = []

for y in range(m):
    for x in range(n):
        # 아직 방문하지 않았으면
        if maps[y][x] == 0 and (x, y) not in visit:
            area = bfs(x, y) # 해당 영역의 넓이
            results.append(area)

print(len(results))
for k in sorted(results):
    print(k, end=' ')
