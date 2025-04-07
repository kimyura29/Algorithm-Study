import sys
input = sys.stdin.readline

n = int(input()) # 컴퓨터 개수
v = int(input()) # 쌍(선)의 개수
graph = [[] for _ in range(n+1)] # 그래프 2차원 리스트로 초기화 => 1번 컴터를 1번 인덱스 쓰려고(n+1)

visted = [0] *(n+1) # 방문한 컴퓨터인지 확인하는 리스트

# 연결된 컴퓨터 번호 입력받기
for i in range(v): # 그래프 생성
    a, b =map(int, input().split())
    graph[a] += [b] # a에 b 연결
    graph[b] += [a] # b에 a 연결(쌍방 연결 표시)

def dfs(v):
    visted[v]=1 # 방문표시
    for j in graph[v]:
        if visted[j]==0:
            dfs(j)
        
dfs(1) # 1번 컴퓨터와 연결된 컴터 = 1
print(sum(visted)-1) # 1번 컴퓨터 제외