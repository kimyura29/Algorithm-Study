import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]

nums.sort() # [-2,1,2,3,8]

# 산술평균
print(round(sum(nums)/n)) # 정수 반올림

# 중앙값
print(nums[(n-1)//2])

# 최빈값
count = Counter(nums)
mode_freq = count.most_common() # [(1, 3), (2, 2), (3, 1)] 이렇게 빈도순 정렬
max_count = mode_freq[0][1] # 3회겠지?
modes = [num for num, freq in mode_freq if freq == max_count] # 지금 최빈값과 동일한 num들 담김

if len(modes) >= 2:
    print(modes[1])
else:
    print(modes[0])

# 범위
print(nums[-1]-nums[0])