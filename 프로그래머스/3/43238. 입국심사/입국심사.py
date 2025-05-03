def solution(n, times):
    left = 1
    right = max(times) * n # 총 걸린 시간(일단 최대로)
    answer = right # 초기화
    
    while left <= right:
        mid = (left + right) // 2
        total = sum(mid // t for t in times) # 총 시간 // 한 심사관이 심사하는 시간 = 몇 명 가능한지      
        if total >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
        
    return answer
