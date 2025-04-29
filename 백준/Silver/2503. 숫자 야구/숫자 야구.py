import sys
input = sys.stdin.readline
n = int(input())


def baseball(hints):
    count = []
    for answer in range(123,988): # 987까지 포함
        answer_str = str(answer)
        if '0' in str(answer) or len(set(str(answer))) !=3:
            continue # 건너뛰기

        # 후보마다 number, s, b 검사
        is_possible=True
        for number, s, b in hints:
            number = str(number)
            # 스트라이크 개수 세기
            strike = 0
            for i in range(3):
                if answer_str[i] == number[i]:
                    strike += 1
            # 볼 개수 세기
            ball = 0
            for i in range(3):
                if answer_str[i] != number[i] and answer_str[i] in number:
                    ball += 1
            # 만일 하나라도 조건에 맞지 않다면
            if strike != s or ball != b:
                is_possible = False
                break
        # 여러 hint중 조건이 맞다면 count에 추가    
        if is_possible:
            count.append(answer)
    
    return len(count)

hints = []
for _ in range(n):
    number, s, b = map(int, input().split())
    hints.append((number, s, b))

print(baseball(hints))