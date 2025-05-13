import sys
input = sys.stdin.readline

a, b = map(int,input().split())


def sol(a,b):
    count = 0 # 연산 횟수
    while b >= a:
        if b == a:
            return count + 1
        if b % 2 == 0:
            b = b // 2
            count += 1
        # 만약 맨 뒷자리가 1이라면, 뒷자리 1을 뺀다
        elif str(b)[-1] == '1':
            b = int(str(b)[:-1])
            count += 1
        # 만약 만들 수 없으면 
        else:
            return -1
    return -1
        
print(sol(a,b))        