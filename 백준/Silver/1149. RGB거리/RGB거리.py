import sys
input = sys.stdin.readline
n = int(input())
price = [list(map(int, input().split())) for _ in range(n)] # n행 3열 2차원 리스트
dp = [[0] * 3 for _ in range(n)] # 누적 비용 2차원 리스트 만들어주자
dp[0][0] = price[0][0]
dp[0][1] = price[0][1]
dp[0][2] = price[0][2]
def sol(n):
    for i in range(1, n): # (i-1)번 사람
        # i번째 사람 r=0일 때
        dp[i][0] = price[i][0] + min(dp[i-1][1], dp[i-1][2]) # 누적 합의 최솟값을 더해주기
        dp[i][1] = price[i][1] + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = price[i][2] + min(dp[i-1][0], dp[i-1][1])
        
    return min(dp[n-1][0], dp[n-1][1], dp[n-1][2])    
print(sol(n))