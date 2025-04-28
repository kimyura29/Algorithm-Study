import sys
# input = sys.stdin.readline

# n이 여러 개 입력
for line in sys.stdin:
    n = int(line)

    dp = [0] * (n+1) # 인덱스니까 n+1까지
    dp[0] = 1 # 기본
    if n >= 1:
        dp[1] = 1
    if n >= 2:
        dp[2] = 3

    for i in range(3, n+1):
        dp[i] = dp[i-1] + 2 * dp[i-2] 

    print(dp[n])

