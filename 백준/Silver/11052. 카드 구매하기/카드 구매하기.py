import sys
input = sys.stdin.readline
n = int(input())
cards = list(map(int,input().split())) 
dp = [0]*(n+1) # 카드 i개 구매할 때 최대 가격
cards = [0] + cards

def solution(n, cards):
    for i in range(1, n+1): # n개 구매할 때
        for j in range(1, i+1): # 최대 i까지(cards에서)
            dp[i] = max(dp[i], dp[i-j]+cards[j])
    return dp[n] # n개 구매할 때 카드 최대값

print(solution(n,cards))

    
