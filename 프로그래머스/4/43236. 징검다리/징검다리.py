def solution(distance, rocks, n):
    rocks.sort() # 오름차순 정렬
    rocks = [0] + rocks + [distance]
    left, right = 1, distance
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        prev = 0 # 이전 값
        remove = 0 # 제거할 개수
        for r in rocks[1:]: 
            # (r-prev)이 최솟값인 mid보다 크거나 같으면 다음 검색 진행
            if r - prev >= mid:
                prev = r
            # 만약 최소보다 작으면 바위 제거
            else:
                remove += 1
        # 가능하니까 더 늘려보자
        if remove <= n:
            answer = mid
            left = mid + 1
        # 바위가 너무 많이 제거됐으면 =>mid를 줄이자
        else:
            right = mid - 1
    return answer