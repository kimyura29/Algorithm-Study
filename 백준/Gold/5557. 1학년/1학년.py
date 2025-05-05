import sys
input= sys.stdin.readline
n = int(input())
cal = list(map(int, input().split())) # [8, 3, 2,..]
# 0 ~ 20 이하 수만 가능
dp = [[0] * 21 for _ in range(n-1)] # 만들어야 하는 수 제외 = n-1
dp[0][cal[0]] = 1 # 시작 수 기록

def sol(cal):
    for i in range(1, n-1):
        for j in range(21):
            if dp[i-1][j]: # dp[i-1][j]가 0이 아닌 위치
                if 0 <= j - cal[i] <= 20:
                    dp[i][j - cal[i]] += dp[i-1][j] # 경우의 수 누적
                if 0 <= j + cal[i] <= 20:
                    dp[i][j + cal[i]] += dp[i-1][j]
    

sol(cal)
print(dp[n-2][cal[-1]])