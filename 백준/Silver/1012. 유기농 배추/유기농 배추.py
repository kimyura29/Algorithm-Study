import sys
from collections import deque
input = sys.stdin.readline


# 방향벡터 설정(상하좌우)
dx = [0,0,1,-1]
dy = [1,-1,0,0]



def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    visit.add((x,y)) # 방문 처리

    while queue:
        cx, cy = queue.popleft()

        # 상하좌우 
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            # 1. 방문이 가능한지 
            if nx < 0 or nx >= m or ny <0 or ny >= n:
                continue

            # 2. 중복 체크 (방문한적이 있는지)
            if (nx, ny) not in visit and maps[ny][nx] == 1: # 2차원 배열은 [y][x] 순 🌟
                queue.append((nx, ny))
                visit.add((nx, ny))

# 테스트 케이스
t =  int(input())

# 입력 받기
for _ in range(t):
    m, n, k =  map(int, input().split()) # m: 가로, n: 세로
    maps = [[0]*m for _ in range(n)] # [[0,0,0...],..] 이렇게 2차원 리스트로 채움

    for _ in range(k):
        x, y = map(int, input().split())
        maps[y][x] = 1
    
    visit = set() # 테스트 케이스마다 visit 초기화 해줘야 해🌟

    count = 0 # 지렁이수 계산
    for y in range(n): # 세로 범위(행)
        for x in range(m): # 가로 범위(열)
            # 배추가 있고, 아직 방문하지 않았을 때
            if maps[y][x] == 1 and (x, y) not in visit:
                bfs(x, y)
                count += 1
        
    print(count)

