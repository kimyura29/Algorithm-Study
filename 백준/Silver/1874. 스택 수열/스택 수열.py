import sys
input = sys.stdin.readline

n = int(input())
sequence = [] # 리스트로 저장
for _ in range(n):
    sequence.append(int(input()))

# stack = [int(input()) for _ in range(n)] 와 동일

# [4,3,6,8,7,5,2,1]

# 1. 스택을 이용해 1~n 숫자를 차례대로 push
# 2. 목표 숫자(sequence)를 순서대로 하나씩 확인하면서 위 작업 반복
stack = []
result = []
start = 1
for num in sequence:
    while start <= num:
        stack.append(start)
        result.append('+')
        start += 1

    # 스택이 비어있지 않을 때(stack=True)
    if stack and stack[-1] == num:
        stack.pop()
        result.append('-')

    # 3. 만약 스택의 top이 목표 숫자보다 크고, 이미 그 숫자를 pop해버린 경우면, NO 출력
    else:
        print('NO')
        sys.exit()
        
for r in result:
    print(r)



