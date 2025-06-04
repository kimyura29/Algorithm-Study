import sys
input = sys.stdin.readline
t = int(input())
# a 300 b 60 c 10
# 최소 누르기
a, b, c = 0, 0, 0

# 10의 배수가 아니면 -1
if t % 10 != 0:
    print(-1)
else:
    a = t // 300
    t %= 300
    b = t // 60
    t %= 60
    c = t // 10
    print(a, b, c)