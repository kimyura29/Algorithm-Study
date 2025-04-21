import sys
input = sys.stdin.readline

# 현재 랜선, 만들어야 하는 랜선 수
k, n = map(int, input().split())
# k개의 랜선 길이 저장
lan = [] 
for _ in range(k):
    lan.append(int(input()))
# 1. 정렬하기
lan.sort()

# 길이를 기준으로 이진 탐색하면서
# 각 길이마다 자를 수 있는 랜선 개수를 계산해 n개 이상 만들 수 있는 최대 길이를 찾아라
min_length, max_length = 1, lan[-1]

# 최대 랜선 길이 저장
answer = 0 
# 이진 탐색
while min_length <= max_length:
    mid = (min_length + max_length) // 2 # python은 정수오버플로우가 없으니까 이렇게 써도 돼
    # 중간 길이로 잘랐을 때 만들어지는 총 랜선 수
    count = sum(l//mid for l in lan)

    # n개 이상 만들 수 있다면 => 더 크게 만들어보자
    if count >= n:
        answer = mid # 가능한 길이 일단 저장
        min_length = mid + 1 # 더 긴 길이가 가능한지 확인 => 오른쪽 탐색
    else:
        max_length = mid - 1 # 개수가 부족하니까 길이 줄여서 => 왼쪽 탐색

print(answer)