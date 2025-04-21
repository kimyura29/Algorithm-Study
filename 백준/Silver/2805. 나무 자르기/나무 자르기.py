import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tree_height = list(map(int, input().split()))

# 정렬(오름차순)
tree_height.sort()

min_h, max_h = 0, tree_height[-1]
answer = 0

while min_h <= max_h:
    mid = (max_h + min_h) // 2
    count = 0 # 나무 총 길이
    for t in tree_height:
        # 나무 높이가 자르는 높이 보다 클 때만
        if t > mid:
            count += (t-mid)
    # count = sum((t-mid) for t in tree_height if t > mid) 와 같음

    if count >= m: # 길이가 길 때 => mid가 더 커져서 더 많이 잘라야 해
        answer = mid # 현재 높이도 정답 후보
        min_h = mid + 1 # 더 길게 자를 수 있는지 확인
    else: 
        max_h = mid - 1

print(answer)