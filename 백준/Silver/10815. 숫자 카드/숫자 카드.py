import sys
input = sys.stdin.readline

n = int(input())
n_list = set(map(int, input().split())) # {2, 3, 6, 10, -10} 자동 정렬
m = int(input())
m_list = list(map(int,input().split()))
# [6,3,2,10,-10]
# [10, 9, -5, 2, 3, 4, 5, -10]

for num in m_list:
    print(1 if num in n_list else 0)