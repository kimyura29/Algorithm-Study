import math
def solution(progresses, speeds):
    result = []
    count = 1 # 첫 작업
    p = len(progresses)
    for i in range(p):
        days = math.ceil((100-progresses[i]) / speeds[i]) # 남은 작업량 / 속도 => '올림' 필요
        result.append(days)
    now = result[0] # 제일 첫 번째 작업
    answer = [] # 배포 수
    # 두 번째 작업부터 검사
    for j in range(1, p):
        # 현재 작업 < 다음 작업
        if now < result[j]:
            # now보다 큰 작업이 나오면 지금까지의 count를 answer에 저장
            answer.append(count)
            # 새로운 그룹이 시작되면, 현재 작업 하나 들어간거니까 
            count = 1 # count = 1로 초기화
            now = result[j]  # 그리고 now도 새 기준으로 바꿔줌
        else:
            # now보다 작거나 같으면, 같이 배포하니까
            count += 1 # now는 갱신 필요 x
    answer.append(count)
    return answer