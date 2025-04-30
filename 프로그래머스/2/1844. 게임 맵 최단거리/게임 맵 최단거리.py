from collections import deque
# 방향벡터
dx = [0, 0 ,1, -1]
dy = [1, -1, 0, 0]

def solution(maps):
    queue = deque()
    visit = set() # 방문처리
    queue.append((0,0,1)) # x,y,칸 수
    visit.add((0,0))
    n, m = len(maps[0]),len(maps) # 열,행
    while queue:
        cx, cy, cd = queue.popleft()
        if cx == n-1 and cy == m-1:
            return cd
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            # 경계값 체크
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 아직 방문 안했고, 지날 수 있는 칸
            if (nx,ny) not in visit and maps[ny][nx] == 1:
                queue.append((nx, ny, cd+1))
                visit.add((nx, ny))
    # 큐가 다 비었는데 도달을 못했으면
    return -1
                