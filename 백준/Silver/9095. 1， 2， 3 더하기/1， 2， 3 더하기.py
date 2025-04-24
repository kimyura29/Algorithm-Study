import sys
input = sys.stdin.readline

t = int(input()) 
for _ in range(t):
    plus = int(input())
    dp = [0] * (plus+1) # 1차원 dp 리스트
    # 시작점
    dp[0] = 1 # 합이 0인 경우는 1가지 => 아무것도 더하지 않는 방법(기저사례)
    # IndexError방지
    if plus >= 1:
        dp[1] = 1
    if plus >= 2:
        dp[2] = 2
    if plus >= 3:
        dp[3] = 4

    for i in range(4,plus+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    print(dp[plus])