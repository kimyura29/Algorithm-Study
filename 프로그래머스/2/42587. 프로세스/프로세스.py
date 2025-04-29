from collections import deque
def solution(priorities, location):
    queue = deque([(idx, p) for idx, p in enumerate(priorities)]) # queue에 인덱스와 중요도 넣기
    order = 0 # 순서
    # queue가 빌때까지 반복
    while queue:
        now = queue.popleft() # 가장 처음 친구 빼
        # now의 p를 기준으로 queue의 p가 더 큰게 하나라도 있다면?
        if any (now[1] < q[1] for q in queue):
            queue.append(now)
        else:
            order += 1
            if now[0] == location:
                return order
                # break