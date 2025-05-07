from functools import cmp_to_key
# 비교 함수 정의
def compare(a, b):
    if a + b > b + a:
        return -1  # a가 먼저 와야 해 => 내림차순
    elif a + b < b + a:
        return 1   # b가 먼저 와야 함=> 오름차순
    else:
        return 0   # 같음

def solution(numbers):
    # 1. 숫자 → 문자열로 변환
    numbers = list(map(str, numbers))
    # 2. 비교 함수를 기준으로 정렬
    numbers.sort(key=cmp_to_key(compare))
    # 3. 이어 붙이고, 0 처리
    return str(int(''.join(numbers)))
