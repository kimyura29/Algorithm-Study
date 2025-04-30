import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10**6)

# 방향벡터
dx = [0, 0 ,1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y):
    visit.add((x,y))
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx <m and 0 <= ny < n:
            if (nx, ny) not in visit and cabbage[ny][nx] == 1:
                dfs(nx, ny) # 방문처리는 dfs내에서 함

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    cabbage = [[0] * m for _ in range(n)]
    visit = set()
    count = 0 # 개수

    for _ in range(k):
        x, y = map(int, input().split())
        cabbage[y][x] = 1

    
    for i in range(n): # 행
        for j in range(m): # 열
            if (j, i) not in visit and cabbage[i][j] == 1:
                dfs(j,i)
                count += 1
    print(count)
    
    
