import sys
import copy
from collections import deque
from itertools import combinations 
input = sys.stdin.readline
n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)] # 연구실 지도


# 방향 벡터
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(maps):
    queue = deque()
    for i in range(n): # 행
        for j in range(m): # 열
            # 바이러스인 연구소 입력하기
            if maps[i][j] == 2:
                queue.append((j,i))
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if maps[ny][nx] == 0:
                maps[ny][nx] = 2 # 감염됨
                queue.append((nx, ny))

# 0의 개수 세는 함수    
def count_0(board):
    count = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                count += 1
    return count


wall_comb = [] # 빈칸 좌표
# 0-> 1 벽으로 변경할 3개 고르기 => 조합
for i in range(n): # 행
    for j in range(m): # 열
        if maps[i][j] == 0:
            wall_comb.append((i,j))

answer = [] # 조합들의 0의 개수
for walls in combinations(wall_comb, 3):
    # 매번 새 복사본을 사용
    temp = copy.deepcopy(maps) # temp = maps에서 1을 변경한 배열 
    # 벽 세우기
    for i, j in walls:
        temp[i][j] = 1
    
    # 바이러스 퍼뜨리고 0 개수 세자
    bfs(temp)
    answer.append(count_0(temp))

print(max(answer))
