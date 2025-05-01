import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
# 방향벡터
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
# DFS로 풀어보기 => 재귀
visit = set()
def dfs(x, y):
    visit.add((x,y))
    cnt = 1 # 칸수 세기(시작점 포함)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 1. 경계선 체크
        if 0 <= nx <= n-1 and 0 <= ny <= m-1:
            # 2. 방문가능한지
            if (nx, ny) not in visit and maps[ny][nx] == 1:
                visit.add((nx, ny))
                cnt += dfs(nx, ny) # dfs돌아가는 횟수만큼 넓이 누적
    return cnt


m, n, k = map(int,input().split())
maps = [[1]*n for _ in range(m)] # nXm 으로 2차원 리스트 만들기
for _ in range(k):
    x1, y1, x2, y2 = map(int,input().split())
    for i in range(y1, y2): # 행
        for j in range(x1, x2): # 열 
            maps[i][j] = 0 # 색칠된 부분 0으로 채우기

result = []
for y in range(m): # 행
    for x in range(n): # 열 
        if (x, y) not in visit and maps[y][x]==1:
            r = dfs(x,y)
            result.append(r)

result.sort()
print(len(result))
print(*result)
    

