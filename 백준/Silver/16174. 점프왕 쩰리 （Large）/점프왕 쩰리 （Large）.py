import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]

queue = deque()
queue.append([0,0])  # 시작점을 큐에 추가

visited = [[0]*N for _ in range(N)]  # 중복 방문 방지용 (optional)

while queue:
    x, y = queue.popleft() # 리스트 언패킹
    
    # 현재 칸의 이동 거리
    jump = graph[x][y]
    if jump == 0:
        continue  # 이번 반복은 여기서 끝내고, 다음 반복으로 넘어가    
    # 도착 조건 :위치가 -1
    if graph[x][y] == -1:
        print("HaruHaru")
        exit() # 프로그램 전체 종료
    
   
    # 아래로 이동
    if 0 <= x + jump < N:
        if visited[x + jump][y] == 0:
            queue.append([x + jump, y])
            visited[x + jump][y] = 1
            
    # 오른쪽으로 이동
    if 0 <= y + jump < N:
        if visited[x][y + jump] == 0:
            queue.append([x, y + jump])
            visited[x][y + jump] = 1

print("Hing")
