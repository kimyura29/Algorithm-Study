import sys
input = sys.stdin.readline

n = int(input())
num_n = set(map(int, input().split())) # [4,1,5,2,3] 이렇게 저장
m = int(input())
num_m = list(map(int, input().split()))

for i in num_m:
    if i in num_n:
        print(1)
    else:
        print(0)