import sys
input = sys.stdin.readline

n, x = map(int,input().split())
A = list(map(int, input().split()))

result =[] 

for i in range(n):
    if A[i] < x:
        result.append(A[i])

print(*result) # 원래 [1, 4, 2, 3]으로 출력되는거 1 4 2 3 으로 출력시킬 때