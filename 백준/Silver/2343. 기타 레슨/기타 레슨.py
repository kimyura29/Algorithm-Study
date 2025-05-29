import sys

input = sys.stdin.readline
n,m = map(int, input().split())
blue = list(map(int,input().split()))



# 블루레이마다 들어간 강의 총 길이의 최대값을 최소화하는 게 목표
# 블루레이의 강의의 길이로 이진탐색 진행
# 우선 blue의 최대 길이의 강의는 무조건 하나의 블루레이에 들어가 => left = max(blue)
# right => blue의 모든 강의 합친 것

def sol(blue, m, n):
    left, right = max(blue), sum(blue) 
    answer = right 
    while left <= right:
        mid = (left+right) // 2 # 이 mid값이 강의의 최대 길이라고 생각하고 검사
        # 가능하다면 더 작게 도전
        # m개로 나눌 수 있는지 test
        def test(blue, m, max_leng):
            count = 1 # 블루레이 개수
            length = 0 # 블루레이 각 길이
            for i in blue:
                # 블루레이 최대 길이보다 작다면 누적
                if length + i <= max_leng:
                    length += i
                # 블루레이 최대 길이보다 크다면
                else:
                    count += 1
                    length = i # 새 블루레이를 시작하면서 i 담기
            return count <= m
        if test(blue, m, mid):
            answer = mid
            right = mid-1
        else:
            left = mid + 1
        
    return answer

print(sol(blue, m, n))