import sys
input = sys.stdin.readline

while True:
    pal = input().strip() # 한 줄씩 입력받기(문자열이니까 개행문자 제거)

    if pal == '0': # 입력종료 조건
        break

    if pal == pal[::-1]: # 문자열을 뒤집어서 비교
        print('yes')
    else:
        print('no')
