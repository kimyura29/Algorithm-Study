import sys
input = sys.stdin.readline

n = int(input()) # n개의 도시
cost = [list(map(int, input().split())) for _ in range(n)] # 2차원 비용 행렬

min_cost = float('inf') # 최소비용 초기화
visit = [0] * n # 방문 체크

'''
출발점 설정
한번 갔던 도시는 다시 갈 수 없어(출발점으로 돌아오는 것 제외)
cost[i][j] > 0 OR i에서 j로 갈 수 없는 경우: cost[i][j] = 0
지금 0번부터 n-1번까지 모든 도시를 순회해서 다시 출발점으로 돌아오는 방법을 구해야해
cost[i][j] 와 cost[j][i]는 다를 수도 있어
'''

# 가장 적은 비용을 들이는 여행 계획
def dfs(start, now, count, total):
    global min_cost

    if count ==n:
        if cost[now][start]  > 0:  # 마지막 도시에서 출발 도시로 돌아갈 수 있다면
            min_cost = min(min_cost, total + cost[now][start])
        return
    for next in range(n):
        if not visit[next] and cost[now][next] > 0:
            visit[next] = 1 # next 도시 방문 표시
            dfs(start, next, count+1, total + cost[now][next]) # 그 다음 도시로 이동해서 계속 탐색
            visit[next] = 0 # 탐색 끝났으니까 방문 해제 
        
# 모든 도시를 출발점으로 시작
for i in range(n):
    visit[i] = 1 # 1. 방문 표시 
    dfs(i,i,1,0) # start, now, count, total_cost # 2. 재귀호출
    visit[i] = 0 # 3. 돌아와서 방문 해제

print(min_cost)
