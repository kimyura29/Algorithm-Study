import sys
input = sys.stdin.readline

n = int(input())
stack = []
for _ in range(n):
    order = input().split()
    ord = order[0]

    if ord == 'push':
        stack.append(order[1])

    elif ord == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop()) # 가장 위에 있는 정수 빼기
    
    elif ord == 'size':
        print(len(stack))

    elif ord == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
                
    elif ord == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
        
