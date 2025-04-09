import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
result = 666

while True:
    if '666' in str(result): # '666'이 포함되어 있다면(str이 아니면 무조건 1의 자리부터 시작하니까)
        cnt += 1
    
    if cnt == n:
        break
    result += 1

print(result)