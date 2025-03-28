import sys 
input = sys.stdin.readline

n = int(input())
for i in range(n):
    a, string = input().split()
    for j in range(len(string)):
        print(int(a) * string[j], end='')
    print() # 줄넘김
