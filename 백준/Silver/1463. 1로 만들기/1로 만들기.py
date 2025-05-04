import sys
input = sys.stdin.readline
n = int(input())

# n은 1 이상의 수
def sol(n):
    dp = [0] * (n+1)
    if n >= 2: # 정의 안하면 n=1일 때 인덱스 에러남
        dp[2] = 1
    for i in range(3, n+1):
        dp[i] = dp[i-1] + 1 # 일단 가장 큰 값으로 초기화 => 최솟값 구하기니까
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i//3]+1)
        if i % 2 == 0: # 6의 배수는 2,3도 다 나눠지니까 elif아니고 if
            dp[i] = min(dp[i], dp[i//2]+1)
    return dp[n]


print(sol(n))