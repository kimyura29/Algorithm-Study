from collections import deque
# bfs 풀이
def solution(n, computers):
    connect = 0 # 연결된 수
    queue = deque()
    visit = [0] * n
    # 컴퓨터 i=0부터 n-1까지 탐색 시작
    for i in range(n):
        if not visit[i]:
            queue.append((i))
            visit[i] = 1 # 방문처리
            
            while queue:
                now = queue.popleft() 
                for nx in range(n):
                    if computers[now][nx] == 1 and not visit[nx]:
                        visit[nx] = 1 # 방문처리
                        queue.append((nx))
            connect += 1
                        
    return connect