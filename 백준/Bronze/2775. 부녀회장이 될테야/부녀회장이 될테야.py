import sys
input = sys.stdin.readline

t = int(input())
# k,n은 14가 최댓값
# 테이블 만들자(0호는 없지만 인덱스 맞추기 위해 고고)
dp = [[0] * 15 for _ in range(15)]
# dp[0] = [0,0,... 0] 0층 총 15호(0~14호)
# dp[1] = [0,0,...,0] 1층 총 15호
for i in range(1, 15):
    dp[0][i] = i # 0층은 i만큼

for k in range(1,15):
    for n in range(1,15):
        dp[k][n] = dp[k-1][n] + dp[k][n-1]

for _ in range(t):
    k = int(input())
    n = int(input())
    print(dp[k][n])