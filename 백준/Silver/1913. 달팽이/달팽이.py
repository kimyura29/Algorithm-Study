import sys
input = sys.stdin.readline
n = int(input())
m = int(input()) # 출력해야 할 값

# 상우하좌 방향 벡터 => 아래쪽으로 증가하는 y축, 오른쪽으로 증가하는 x축
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

maps = [[0]*n for _ in range(n)]

'''
중앙에서 시작해서 상-> 우 -> 하-> 좌 순서로 1씩 증가하며 채우기(n**2까지)
'''

def sol(n, m):
    # 시작위치
    x = y = n//2
    maps[y][x] = 1
    num = 2 # 2부터 채우기
    length = 1 # 움직일 횟수(1칸, 2칸씩 점점 증가)
    target_x = target_y = x # m의 좌표 저장용
    while num <= n*n:
        for dir in range(4): # 상우하좌 방향
            for _ in range(length):
                x += dx[dir]
                y += dy[dir]
                if not (0 <= x < n and 0 <= y < n):
                    continue
                maps[y][x] = num
                if num == m:
                    target_x = x
                    target_y = y
                num += 1
            # 2번 돌면 길이 1 증가(상->우, 하->좌)
            if dir % 2 == 1:
                length += 1
    return target_y, target_x
    
# 출력하기
target_y, target_x = sol(n,m)
for row in maps:
    print(*row)
print(target_y+1, target_x+1)