import sys
import heapq # 우선순위 큐
from collections import deque
input = sys.stdin.readline
n = int(input()) # 도시 개수
m = int(input()) # 버스 노선 개수
graph = [[] for _ in range(n+1)] # (1~n번) 인접리스트 도시
for _ in range(m):
    s, f, c = map(int, input().split())
    graph[s].append((f, c)) # 이렇게 도착지와 비용 같이 담아
start, final = map(int,input().split()) # 우리가 구해야하는 출발지, 도착지

# 최소비용 구하기
INF = float('inf')
cost = [INF] * (n+1) # 최소 비용 저장용
prev = [0] * (n+1) # 경로 복원용 (도착지점에서 거슬러 올라감)


def solution(start):
    global cost
    cost[start] = 0 # 처음 비용 = 0으로 초기화
    heap = [] # 우선순위큐는 일단 리스트로 선언
    heapq.heappush(heap, (0, start)) # (누적비용, 현재도시)
    while heap:
        cost_so_far, now = heapq.heappop(heap)
        if cost[now] < cost_so_far:
            continue # 이미 더 짧은 경로로 방문됨
        for next_node, c in graph[now]:
            new_cost = cost_so_far + c
            if new_cost < cost[next_node]:
                cost[next_node] = new_cost
                prev[next_node] = now # 경로 추적용
                heapq.heappush(heap, (new_cost, next_node))

solution(start)
print(cost[final]) # 1. 최소비용
# 2. 몇 개의 도시 지났는지 
path = []
current = final
while current != 0:
    path.append(current)
    current = prev[current]
path.reverse()

print(len(path))
# 3. 경로 반환 => 값만
print(*path)  