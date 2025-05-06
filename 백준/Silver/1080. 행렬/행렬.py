import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a_map = [list(map(int, input().strip())) for _ in range(n)] # 2차원 배열
b_map = [list(map(int, input().strip())) for _ in range(n)]


def sol(n,m):
    global a_map
    count = 0 # 뒤집는 횟수
    # 3x3 행렬 반전시키기
    def flip(maps, x, y):
        for i in range(x, x+3):
            for j in range(y, y+3):
                maps[i][j] = 1- maps[i][j] # 0->1, 1->0 비트 뒤집기
        return maps
    # 일단 n,m이 3보다 작으면 return -1
    if n < 3 or m < 3:
        return -1 if a_map != b_map else 0 # 3x3보다 작아도 처음부터 같다면 0 반환
    else:
        for a in range(n-2):
            for b in range(m-2):
                if a_map[a][b] != b_map[a][b]:
                    a_map = flip(a_map, a, b) 
                    count += 1
    if a_map == b_map:
        return count
    else:
        return -1

print(sol(n,m))
        
