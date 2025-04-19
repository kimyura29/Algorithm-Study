import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
counter = Counter(cards) # 카드별 개수 세두기 => 딕셔너리 형태
m = int(input())
count_cards = list(map(int, input().split()))

for target in count_cards:
    print(counter[target], end = ' ')

