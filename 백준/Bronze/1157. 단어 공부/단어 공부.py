import sys
from collections import Counter
input = sys.stdin.readline

# 대소문자 구분하지 x => 소문자로 전부 변환
# 만약 max값이 여러개면 ? 반환
# 대문자로 출력

word = input().strip() # 문자열 받기
word_upper = word.upper() # 대문자로 변환
# word = list(word_upper) # 문자열이 하나하나 리스트 원소로 변환 => 필요 없어

counter = Counter(word_upper) # 문자열 안 개수 세기 => counter는 문자열도 순회 가능
max_count = max(counter.values()) # 가장 많이 나온 원소의 횟수
max_words = [k for k, v in counter.items() if max_count == v] # k는 원소, v는 횟수

if len(max_words) == 1:
    print(max_words[0]) # 리스트로 나오니까 [0]으로 뽑아주자
else:
    print('?')