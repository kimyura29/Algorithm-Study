import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)] # 게임판 구역 2차원 리스트로 초기화

visited = [[0]*n for _ in range(n)] # 방문 여부 처리 리스트

def dfs(x, y):
    # 영역을 벗어났거나 이미 방문을 했다면 return
    if x<=-1 or x>=n or y<=-1 or y>=n or visited[x][y]==1:
        return
    
    # 방문한 곳의 이동 칸 수가 -1이라면 방문 처리를 해주고 return
    if graph[x][y] == -1 :
        visited[x][y] = 1
        return

    # 방문했다고 표시
    visited[x][y]=1

    # 상,하,좌,우를 요소 수만큼 점프하여 방문
    dfs(x + graph[x][y], y)
    dfs(x, y + graph[x][y])    

dfs(0,0) # 출발 지점 호출
if visited[-1][-1] == 1:
    print('HaruHaru')
else:
    print('Hing')