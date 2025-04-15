import sys
from collections import deque
input = sys.stdin.readline

n = int(input()) # n X n 지도
maps = [list(map(int,input().strip())) for _ in range(n)] # 2차원 리스트로 입력받기

# 방향 벡터 설정
dx = [0,0,1,-1]
dy = [1,-1,0,0]

queue = deque()
visit = set()

# 단지에 속하는 집의 수
count_list = []

def bfs(x, y):
    queue.append((x, y))
    visit.add((x, y))
    count = 1 # 단지 수
    while queue:
        # 현재 위치
        cx, cy = queue.popleft()

        # 상하좌우
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
        
            # 1. 방문이 가능한지 -> 경계값 체크(가능한지)  
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            # 2. 중복체크 - 방문한 적이 있는지
            if (nx, ny) not in visit and maps[ny][nx] == 1:
                queue.append((nx, ny))
                visit.add((nx, ny))
                count += 1
    return count

for i in range(n):
    for j in range(n):
        # 집이 있는 곳(1)이고, 아직 방문하지 않았을 때
        if maps[j][i] == 1 and (i, j) not in visit:
            house = bfs(i, j)
            count_list.append(house)

print(len(count_list)) # 총 단지 수
# 단지 내 집의 수(오름차순)
for k in sorted(count_list):
    print(k)



