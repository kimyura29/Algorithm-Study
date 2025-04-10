import sys 
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split()) # 문서 수, 목표 인덱스
    importances = list(map(int, input().split()))  # 중요도 리스트로 저장

    queue = deque([(idx, importance) for idx, importance in enumerate(importances)]) # deque[(인덱스, 중요도),..]
    order = 0 # 순서 카운트

    # 큐가 비어있지 않을 때만 반복
    while queue:
        current = queue.popleft()

        # 뒤에 더 높은 중요도가 있는지
        if any(current[1] < q[1] for q in queue): # any()는 하나라도 true면 전체 true 반환
            queue.append(current)
        else:
            order += 1 # 출력
            if current[0] == m:
                print(order)
                break


