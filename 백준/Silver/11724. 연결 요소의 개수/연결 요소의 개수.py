import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int,input().split())
graph = [[] for _ in range(n+1)] # 간선 개수 = 인덱스 번호 + 1
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# print(graph) [[], [2, 5], [1, 5], [4], [3, 6], [2, 1], [4]]


visit = [0] * (n+1)  # 방문 여부 리스트

def bfs(start):
    queue = deque([start])
    visit[start] = 1
    while queue:
        now = queue.popleft()
        for nx in graph[now]:
            if not visit[nx]:
                visit[nx] = 1
                queue.append(nx)

count = 0
for i in range(1, n+1):
    if not visit[i]:
        bfs(i)
        count += 1

print(count)