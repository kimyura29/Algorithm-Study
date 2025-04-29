from collections import deque
def solution(progresses, speeds):
    result = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    # progresses가 비면 멈춰
    while progresses:
        days = -(-(100-progresses[0]) // speeds[0]) # 올림 적용
        count = 0
        # progresses가 비고 100-pro[0] > sp[0]*days이면 멈춰
        while progresses and (100-progresses[0]) <= speeds[0] * days:
            # 만족하면 popleft
            progresses.popleft()
            speeds.popleft()
            # 한 그룹 끝나면
            count += 1
        result.append(count)
    return result