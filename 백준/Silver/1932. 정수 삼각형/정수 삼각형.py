import sys
input = sys.stdin.readline

n= int(input())
tri = [list(map(int,input().split())) for _ in range(n)]

def sol(n, tri):
    dp = [[0] * n for _ in range(n)]
    dp[0][0] = tri[0][0] # 맨 꼭짓점
    for i in range(1,n):
        # 삼각형 구조니까 j = i+1개
        for j in range(i+1):
            # 왼쪽 위 없을 때
            if j == 0:
                dp[i][j] = dp[i-1][j] + tri[i][j]
            # 오른쪽 위 없을 때
            elif i == j:
                dp[i][j] = dp[i-1][j-1] + tri[i][j]
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + tri[i][j]
    
    return max(dp[n-1])

print(sol(n, tri))

