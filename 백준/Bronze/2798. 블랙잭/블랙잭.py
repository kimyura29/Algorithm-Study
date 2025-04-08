import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
cards = list(map(int, input().split()))

result = 0
for combo in combinations(cards,3):
    total = sum(combo)
    if total <= m:
        result = max(result, total)
        
print(result)
