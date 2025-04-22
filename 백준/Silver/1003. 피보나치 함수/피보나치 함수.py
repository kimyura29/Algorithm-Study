import sys
input = sys.stdin.readline

t = int(input())
fibo_test = []
for _ in range(t):
    fibo_test.append(int(input()))
# [0,1,3]
# fibo(0) => zero_count[n]
# fibo(1) => one_count[n]
# n마다 0과 1의 호출 횟수를 저장하는 dp 배열 만들자

max_n = max(fibo_test)
zero = [0] * (max_n + 1)
one = [0] * (max_n + 1)

# 초기값 설정
# fibo(0) 에서
zero[0] = 1
one[0] = 0

if max_n >= 1:
    zero[1] = 0
    one[1] = 1

# dp로 개수 채우기
for i in range(2, max_n + 1):
    zero[i] = zero[i-2] + zero[i-1]
    one[i] = one[i-2] + one[i-1]

for j in fibo_test:
    print(zero[j], one[j])
