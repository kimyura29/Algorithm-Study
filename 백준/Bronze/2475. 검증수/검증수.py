import sys
input = sys.stdin.readline

A = list(map(int, input().split())) # 한 줄로 여러 개의 숫자 입력받기(리스트)

result = 0
for i in range(len(A)):
    result += A[i]**2

print(result%10)