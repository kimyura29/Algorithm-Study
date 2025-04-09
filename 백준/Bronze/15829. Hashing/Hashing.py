import sys
input = sys.stdin.readline

n = int(input())
s = input().strip()
r = 31
m = 1234567891

result = 0
for i in range(n):
    alpha = ord(s[i]) - ord('a') + 1 # 알파벳 a,b,c...= 1,2,3...
    result += alpha * (r **(i)) # i는 인덱스니까
print(result % m)
