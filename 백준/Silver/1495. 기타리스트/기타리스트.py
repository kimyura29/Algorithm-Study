import sys
input = sys.stdin.readline

# n개의 곡, 시작 볼륨, 볼륨 최댓값
n, s, m = map(int, input().split())
v_list = list(map(int, input().split()))

# 볼륨
dp = [[0]*(m+1) for _ in range(n+1)] # (n+1)x(m+1) => 2차원 리스트 만들기

# dp[i][v] i번째 곡의 현재 볼륨
# 처음 곡 시작 전 볼륨 설정
dp[0][s] = 1

for i in range(n): # i번째 곡
    for v in range(m+1): # 볼륨
        if dp[i][v] == 1:
            if v + v_list[i] < (m+1):
                dp[i+1][v+v_list[i]] = 1
            if v - v_list[i] >= 0:
                dp[i+1][v-v_list[i]] = 1

# 중간에 볼륨 조절이 안되는 경우
result = -1
# m부터 0까지 탐색
for v in range(m, -1, -1):
    if dp[n][v] == 1:
        result = v
        break
print(result)