import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
candy = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*m for _ in range(n)] 
def sol(n,m):
    for i in range(n): # 행
        for j in range(m): # 열
            if j > 0:
                # 오른쪽으로 이동
                dp[i][j] = max(dp[i][j], dp[i][j-1])
            if i > 0:
                # 위로 이동
                dp[i][j] = max(dp[i][j], dp[i-1][j])
            if j > 0 and i > 0:
                # 대각선 이동
                dp[i][j] = max(dp[i][j], dp[i-1][j-1])
            dp[i][j] += candy[i][j] # 현재 사탕 더하기
        
    return dp[n-1][m-1]

print(sol(n, m))