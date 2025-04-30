import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

r, c = map(int, input().split())
maps = [list(input().strip()) for _ in range(r)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

max_count = 0

def dfs(x, y, visited, count):
    global max_count
    max_count = max(max_count, count)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < c and 0 <= ny < r:
            alpha = ord(maps[ny][nx]) - ord('A')  # 알파벳을 0~25 정수로 변환
            if not (visited & (1 << alpha)):  # 방문 안 했으면
                dfs(nx, ny, visited | (1 << alpha), count + 1)

# 시작 알파벳 방문 표시
start = ord(maps[0][0]) - ord('A')
dfs(0, 0, 1 << start, 1)
print(max_count)