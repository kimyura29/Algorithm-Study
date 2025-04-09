import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
result = 666

while True:
    if '666' in str(result): # '666'이 포함되어 있다면(숫자 패턴 찾기 쉽게 str로)
        cnt += 1
    
    if cnt == n:
        break
    result += 1

print(result)