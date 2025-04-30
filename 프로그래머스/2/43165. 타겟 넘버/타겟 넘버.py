def solution(numbers, target):
    answer = 0 # 결과 저장
    def dfs(index, total):
        nonlocal answer # 바깥함수의 변수 사용
        # 종료 조건: 모든 수 사용
        if index == len(numbers):
            # 더한 수가 target과 같으면
            if total == target:
                answer += 1
            return
        # 더하기 연산 후 다음 숫자로 이동
        dfs(index+1, total+numbers[index])

        # 빼기 연산 후 다음 숫자로 이동
        dfs(index+1, total-numbers[index])
    
    dfs(0,0) # index=0부터, total=0부터 시작
    
    # 결과 반환
    return answer