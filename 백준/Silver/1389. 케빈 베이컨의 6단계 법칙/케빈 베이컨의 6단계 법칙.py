import sys
input= sys.stdin.readline
from collections import deque
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)] # 인접리스트 만들기 (0~n)번 
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b) # (a)인덱스에 아는 사람 입력
    graph[b].append(a) # 양방향 그래프임(친구사이)


def bfs(start):
    queue = deque()
    visit = [0] * (n+1) # 친구 거리 누적용
    queue.append(start)
    while queue:
        cx = queue.popleft()
        for nx in graph[cx]: # cx의 존재하는 친구들만 순회
            # 아직 방문하지 않았고, 자기 자신으로 되돌아가는 경로가 아니라면
            if not visit[nx] and nx != start:
                visit[nx] = visit[cx] + 1 # cx의 친구 nx는 cx보다 한단계 더 멀리 있음 → 거리 +1
                queue.append(nx) # nx 탐색 시작해보자
             
    return visit

bacon = []
for i in range(1,n+1):
    bacon.append(sum(bfs(i)))

min_value = min(bacon)
min_index = bacon.index(min_value) # 제일 처음 인덱스 나올거야
print(min_index + 1) # 인덱스 +1이 사람 번호