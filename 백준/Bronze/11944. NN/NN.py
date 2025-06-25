import sys
input = sys.stdin.readline
n, m  = map(int,input().split())
string = str(n) * n

print(string[:m])