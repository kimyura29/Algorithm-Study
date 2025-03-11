import sys
def bridge(m, n):
    dp = [[0] * (n+1) for _ in range(m+1)] # (n+1)행 * (m+1)열 배열 만들기 = 2차원 리스트(테이블)

    # 초기화
    for i in range(m+1):
        dp[i][0] = 1 # 0(=1)을 뽑는 경우의 수 1
        if i <= n:
            dp[i][i] = 1 # nCn = 1

    # 테이블 채우기
    for i in range(1, m+1):
        for j in range(1, min(i, n)+1): # j가 i보다 클 수 없어
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

    return dp[m][n]

T = int(sys.stdin.readline().strip())

for _ in range(T):
    n, m = map(int, sys.stdin.readline().split())
    print(bridge(m,n))