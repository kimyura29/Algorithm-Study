import sys
from collections import deque
input = sys.stdin.readline

n,m,t = map(int, input().split())
maps = [list(map(int,input().split())) for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def sol(n,m,maps):
    queue = deque()
    # visit[y][x][0] = 그람 보유 x/ visit[y][x][1] = 그람 보유 o
    visit = [[[0]*2 for _ in range(m)] for _ in range(n)]
    # (x,y,cnt, gram보유여부)
    queue.append((0,0,0,0)) # x,y,cnt
    visit[0][0][0] = 1
    while queue:
        cx, cy, cnt, gram = queue.popleft()
        # 시간 초과
        if cnt > t:
            continue
        # 공주에게 도달하면
        if cx == m-1 and cy == n-1:
            return cnt
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                cell = maps[ny][nx]
                state = 1 if gram==1 else 0 # 그람 지났을 때 state는 1

                # 이미 방문했으면 skip
                if visit[ny][nx][state] == 1:
                    continue
                # 아직 그람 줍지 않았을때, cell==1이면 통과
                if gram ==0 and cell == 1:
                    continue

                # 그람 주움
                if cell == 2:
                    visit[ny][nx][1] = 1
                    queue.append((nx,ny,cnt+1,1))
                # 그람 줍지 않고, cell이 0일때
                else:
                    visit[ny][nx][state] = 1
                    queue.append((nx, ny, cnt+1, state))
    return None


count = sol(n,m,maps)
if count != None and count <= t:
    print(count)
else:
    print('Fail')



