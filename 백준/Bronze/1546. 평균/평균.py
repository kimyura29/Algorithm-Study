import sys
input = sys.stdin.readline

n = int(input())
score = list(map(int, input().split()))

avg = 0
# scores 오름차순 정렬해서 scores[-1]
max_score = max(score)
for s in score:
    avg += s/max_score * 100
print(avg/n)
