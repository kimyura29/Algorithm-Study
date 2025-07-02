import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
maps = []
for i in range(n):
    row = list(map(int, input().split()))
    maps.append(row)
# print(maps) 

def bfs(maps, n, m):
    result = [[-1] * m for _ in range(n)] # 정답판 초기화
    queue = deque()

    # 목표지점 찾기
    for y in range(n): # 행
        for x in range(m): #열
            if maps[y][x] == 2:
                queue.append((x,y)) # 시작점
                result[y][x] = 0 # 자기 자신까지 거리

    # 방향 벡터 (2차원)
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            # 경계값체크
            if 0 <= nx < m and 0 <= ny < n:
                # 방문 가능한지
                if maps[ny][nx] == 1 and result[ny][nx] == -1:
                    queue.append((nx, ny))
                    result[ny][nx] = result[cy][cx] + 1
    # 갈수없는 땅 = 0 인땅 처리            
    for y in range(n): 
        for x in range(m):
            if maps[y][x] == 0:
                result[y][x] = 0
    return result

res = bfs(maps, n, m)
for row in res:
    print(*row)