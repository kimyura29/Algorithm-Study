import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]


answer = [[0]*n for _ in range(n)]    
def bfs(start):
    queue = deque()
    visit = [0] * n
    queue.append(start)
    while queue:
        node = queue.popleft()
        for nx in range(n):
            if not visit[nx] and maps[node][nx] == 1:
                answer[start][nx] = 1 # start행이야
                visit[nx] = 1 # 방문처리
                queue.append(nx)
                

for i in range(n):
    bfs(i)

for row in answer:
    print(*row)
