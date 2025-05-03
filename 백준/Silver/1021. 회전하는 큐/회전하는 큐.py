import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
locate = list(map(int, input().split()))
# queue = [i for i in range(1,n+1)]
dq = deque(range(1,n+1))
count = 0
for target in locate:
    i = dq.index(target) # dq에서의 인덱스
    # 2번 수행
    if i <= (len(dq) // 2):
        dq.rotate(-i) # 왼쪽 회전
        count += i
    # 3번 수행
    else:
        # 오른쪽 회전
        dq.rotate(len(dq)-i) # 오른쪽 회전
        count += len(dq)-i
    
    dq.popleft() # 목표숫자 제거
print(count)

