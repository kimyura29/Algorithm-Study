import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)] # 정점 개수 + 1 = 인덱스 일치시키게

visited_d = [0] * (n+1) # 방문확인 리스트(dfs)
visited_b = [0] * (n+1) # 방문확인 리스트(bfs)
# 간선 입력받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 각 정점들에 연결된 점들 오름차순 정렬 => 작은 정점부터 방문
for i in range(1, n+1):
    graph[i].sort()
    
# dfs
result_d = []
def dfs(k):
	visited_d[k] = 1 # 방문표시
	result_d.append(k)
	for j in graph[k]: # v번 연결된 정점들 방문 확인
		if visited_d[j] == 0:
			dfs(j)

# bfs
result_b = []
def bfs(k):
    queue = deque([k]) # queue = [k]로 초기화
    visited_b[k] = 1 # 방문 표시
    # queue에 값이 있으면 True, 비면 False로 중단 
    # while문 종료 조건 : deque([]) 
    while queue:
        now = queue.popleft() # 맨 앞에 있는 정점을 꺼냄
        result_b.append(now)
        for j in graph[now]:
            if visited_b[j] == 0:
                visited_b[j] = 1
                queue.append(j)
	

dfs(v)
print(*result_d)
bfs(v)
print(*result_b)