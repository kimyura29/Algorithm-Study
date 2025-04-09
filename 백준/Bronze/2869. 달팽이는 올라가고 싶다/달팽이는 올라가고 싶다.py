import sys
import math
input = sys.stdin.readline

a, b, v = map(int, input().split())

# 일수 구하는거니까 소숫점은 올림(+1) => math.ceil함수 사용
print(math.ceil((v-b)/(a-b))) # 마지막 날(정상올랐을 때)은 미끄러지지 않으니까: v-b