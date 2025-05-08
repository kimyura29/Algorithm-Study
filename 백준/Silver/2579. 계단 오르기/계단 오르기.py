import sys
input= sys.stdin.readline
n = int(input())
step = []
for _ in range(n):
    step.append(int(input())) # 정수로 리스트에 담기
step = [0] + step # 헷갈려서 길이 맞춤 [0,10,20,15,25,10,20]

def sol(n, step):
    dp = [0] * (n+1) # dp[i] = (i)번째 계단에서의 점수
    if n >= 1:
        dp[1] = step[1]  # 1번째 계단
    if n >= 2:  
        dp[2] = step[2] + step[1] # 일단 2번째 계단에 왔을 때
    if n >= 3:
        # 세 번째 계단에 왔을 때 점수
        dp[3] = max(step[2] + step[3], step[1] + step[3])

    for i in range(4, n+1):
        # (i-2,i)밟을 때/ (i-3,i-1,i)밟을 때
        dp[i] = max(dp[i-2]+step[i], dp[i-3]+step[i-1]+step[i])
    
    return dp[n]

print(sol(n, step))