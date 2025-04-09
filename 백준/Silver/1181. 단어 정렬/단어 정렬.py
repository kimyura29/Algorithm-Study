import sys
input = sys.stdin.readline

n = int(input())
words = [input().strip() for _ in range(n)]

words = list(set(words))

words.sort(key = lambda x: (len(x), x)) # 길이 먼저 비교, 같다면 x 그 자체(알파벳 순) 비교해 정렬
for word in words:
    print(word)