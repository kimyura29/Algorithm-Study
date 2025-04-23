import sys
from collections import deque
input = sys.stdin.readline

def bfs(num):
    dq = deque()
    visit = set() # 테스트 케이스가 여러 개니까
    dq.append(num)
    visit.add(num)

    while dq:
        current = dq.popleft()
        next = permutation[current]
        if next not in visit:
            visit.add(next)
            dq.append(next)
    return visit # 이 사이클에 포함된 노드들


count = 0
t = int(input())
# 입력 받기
for _ in range(t):
    count = 0 # 사이클 개수
    n = int(input())
    visit_perm = set()
    permutation = [0] + list(map(int, input().split())) # [0, 3, 2, 7, 8, 1, 4, 5, 6] 이렇게 넣어야 해
    for i in range(1,n+1):
        if i not in visit_perm:
            cycle = bfs(i)
            visit_perm.update(cycle)
            count += 1
    print(count)
