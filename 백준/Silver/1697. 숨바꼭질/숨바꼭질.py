from collections import deque
n, k = map(int, input().split())

def solution(n, k):
    
    queue = deque()
    queue.append((n,0)) # 위치, 시간
    visit = set()
    count = 0
    while queue:
        cx, ct = queue.popleft()
        if cx == k:
            return ct
        # 경계값 체크
        if cx > 100000:
            continue

        # 방문이 가능한지, 중복체크
        for nx in (cx+1, cx-1, 2* cx):
            # 아직 방문 안했다면
            if not nx in visit:
                queue.append((nx,ct + 1))
                visit.add(nx)

print(solution(n, k))