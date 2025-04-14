import sys
from collections import deque
input = sys.stdin.readline

# 입력 받기
n, m = map(int, input().split())
maps = [list(map(int, input().strip())) for _ in range(n)]

# 2차원일 때 상하좌우 
# 방향 벡터는 리스트로 쓰자
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

queue = deque()
visit = set() # 방문여부

# 시작 x, 시작 y, 현재까지 이동 칸 수
# (값 고정)하게 튜플로 쓰자
queue.append((0,0,1)) # 시작 지점을 한 칸으로 세자
visit.add((0,0)) # set함수는 튜플로 저장(해시 가능)

# queue가 빌 때까지
while queue:
    # 현재 위치, 이동칸수
    cx, cy, cd = queue.popleft()

    # 도착지에서 출력
    if cx == n-1 and cy == m-1: # 도착하면, 인덱스로 설정해서 -1씩
        print(cd) 
        break

    # 상하좌우
    for i in range(4): 
        # 새로 방문하는 x, y
        nx = cx + dx[i]
        ny = cy + dy[i]

        # 1. 방문이 가능한지 -> 경계값 체크(가능한지)  
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        # 2. 중복체크(방문한적이 있는지) 
        # 방문한 적이 없고, 1일 때 => 방문 가능
        if (nx, ny) not in visit and maps[nx][ny] == 1:
            # 새로운 위치, 거리 + 1 
            queue.append((nx, ny, cd+1))
            visit.add((nx, ny))

