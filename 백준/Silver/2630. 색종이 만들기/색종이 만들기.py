import sys
input = sys.stdin.readline
n = int(input())
maps = [list(map(int, input().split())) for i in range(n)]

blue = 0
white = 0

# 색이 모두 같은지 검사
def all_same(x, y, size):
    color = maps[y][x]
    for i in range(y, y+size): # 행
        for j in range(x, x+ size): # 열
            if maps[i][j] != color:
                return False
    return True          
    

# 쪼개서 탐색하는 재귀 함수
def count_paper(x, y, size):
    global blue, white
    # 전체가 색이 동일한지 검사
    if all_same(x,y,size):
        if maps[y][x] == 1:
            blue += 1
        else:
            white += 1
        return  # 여기서 return해야 재귀 종료
    
    # 4등분해서 탐색
    half = size // 2
    count_paper(x, y, half) # 1사
    count_paper(x+half, y, half) # 2사
    count_paper(x, y+half, half) # 3사
    count_paper(x+half, y+half, half) # 4사


count_paper(0, 0, n)

print(white)
print(blue)

