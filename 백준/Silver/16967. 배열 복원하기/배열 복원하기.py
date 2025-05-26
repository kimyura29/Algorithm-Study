import sys
input = sys.stdin.readline
h,w,x,y = map(int,input().split())
b= []
a = [[0]*w for _ in range(h)] # a는 h행, w열
for i in range(h+x):
    b.append(list(map(int,input().split())))

# a를 x축 방향으로 y만큼, y축 방향으로 x만큼 이동시켜 겹친게 b
## b[i][j] = a[i][j] + a[i-y][j-x]
# 뒤집으면 a[i][j] = b[i][j] - a[i-y][j-x]

for i in range(h): # 행
    for j in range(w): # 열
        if i >= x and j >= y: # 행>=x, 열>=y
            a[i][j] = b[i][j] - a[i-x][j-y] # 겹친 부분 복사본 제거
        else:
            a[i][j] = b[i][j] # 겹치지 않으면 그대로 복사

for i in a:
    print(*i)