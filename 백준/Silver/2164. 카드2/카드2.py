import sys
from collections import deque

input = sys.stdin.readline
n = int(input())

# 큐 구현 (선입선출)
queue = deque()

# 큐에 넣기
for i in range(1, n+1):
    queue.append(i)

while len(queue) > 1:
    queue.popleft() # 맨 처음 카드 버림
    queue.append(queue.popleft())

print(queue[0]) # 하나 남은 카드 출력