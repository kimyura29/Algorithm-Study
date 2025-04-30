from collections import deque
def solution(prices): 
    answer = []
    queue = deque(prices)
    
    # 큐가 빌 때까지
    while queue:
        time = 0 # 걸린 초
        price = queue.popleft()
        for q in queue:
            time += 1 # 돌아가는 q만큼 1초 추가
            if price > q:
                break # for문 스탑
        answer.append(time)
    return answer