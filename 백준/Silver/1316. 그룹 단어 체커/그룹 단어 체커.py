import sys
input = sys.stdin.readline
n = int(input())

def check(word):
    bf_word = set()
    prev = ''
    for i in word:
        # 직전값과 같지 않은데
        if i != prev:
            # 이전에 나온 단어면
            if i in bf_word:
                return 0
            bf_word.add(i)
        prev = i
    return 1

answer =[]
for _ in range(n):
    word = input().strip()
    answer.append(check(word))

print(sum(answer))