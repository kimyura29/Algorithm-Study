import sys
input = sys.stdin.readline

n = int(input()) # 분해합

# n의 생성자 찾기
for i in range(1, n+1):
    num = sum(map(int, str(i))) # 각 자릿수의 합
    if n == i + num:
        print(i)
        break  # 가장 작은 생성자를 찾으면 종료 🌟🌟 (안쓰면 여러 개의 i를 찾아 덮여쓰기 될수도)
    
# break가 실행되지 않고 for문이 다 돌았을 때    
else:
    print(0)