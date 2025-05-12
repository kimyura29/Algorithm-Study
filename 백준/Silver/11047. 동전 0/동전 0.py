import sys
input = sys.stdin.readline

n, k = map(int,input().split())
coins = [int(input()) for _ in range(n)]
# print(coins)

coins.sort(reverse=True) # 내림차순 정렬

count = 0
for coin in coins:
    if k >= coin:
        count += k // coin # 이 동전을 몇개 쓸 수 있는가
        k %= coin # k를 나머지로 갱신

print(count)