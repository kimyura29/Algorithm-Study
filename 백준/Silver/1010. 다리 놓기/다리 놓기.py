import math

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    bridge = math.factorial(m) // (math.factorial(m-n) * math.factorial(n))
    print(bridge)