import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
maps = [list(map(str, input().strip())) for _ in range(n)]

# 적록색약 O => R,G 같은 색, B 다른색
# x => R, G, B 다른 색
# 구역 나누기

# 방향벡터
dx = [0, 0, 1,-1]
dy = [1, -1, 0, 0]
visit = set() # 일반인 방문처리
# 일반인
def bfs(x, y, color, visit):
    queue = deque()
    queue.append((x,y))
    visit.add((x,y))
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            # 경계값 체크
            if 0 <= nx < n and 0 <= ny < n:
                if (nx, ny) not in visit and maps[ny][nx] == color:
                    visit.add((nx, ny))
                    queue.append((nx, ny))

visit_clr = set() # 적록색약 방문처리 
# 적록색약 버전일 때
def bfs_clr(x, y, color, visit_clr):
    queue = deque()
    queue.append((x,y))
    visit_clr.add((x,y))
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            # 경계값 체크
            if 0 <= nx < n and 0 <= ny < n:
                if (nx, ny) not in visit_clr:
                    if color in 'RG' and maps[ny][nx] in 'RG':
                        visit_clr.add((nx, ny))
                        queue.append((nx, ny))
                    elif color == 'B' and maps[ny][nx] == 'B':
                        visit_clr.add((nx, ny))
                        queue.append((nx, ny))                        

cnt = 0 # 일반인
cnt_clr = 0 # 적록색약
for i in range(n): # 행
    for j in range(n): # 열
        if (j, i) not in visit:
            bfs(j, i, maps[i][j], visit) # color는 현재 BFS가 출발한 기준점의 색, maps[ny][nx]는 탐색 중인 인접한 좌표의 색
            cnt += 1
        if (j, i) not in visit_clr:
            bfs_clr(j, i, maps[i][j], visit_clr)
            cnt_clr += 1

print(cnt, cnt_clr)