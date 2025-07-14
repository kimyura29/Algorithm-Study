import sys
input = sys.stdin.readline
t, x  = map(int,input().split()) # 교시의 개수: t,  건우가 예약한 교시: x
n = int(input()) # 조원의 수: n
result = 1 # 모든 조원 참석 가능 여부
for _ in range(n):
    k = int(input())
    attend = list(map(int, input().split()))

    if x not in attend:
        result = 0

if result:
    print('YES')
else:
    print('NO')
