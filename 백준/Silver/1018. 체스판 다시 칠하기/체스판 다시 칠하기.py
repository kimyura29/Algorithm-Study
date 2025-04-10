import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [] # 입력 받은 보드판 저장 (2차원)
result = [] # 8X8 체스판에 칠해야 하는 최소 횟수 저장

# n줄 동안 문자열 입력 받기
for _ in range(n):
    board.append(input().strip())

# 전체 보드에서 8x8 조각을 추출
# 8칸이니까 0 ~ n-8 =  range(n-7)
for i in range(n-7):
    for j in range(m-7):
        is_black = 0 # 왼쪽 위가 'B'일 때 칠해야 하는 횟수
        is_white = 0 # 왼쪽 위가 'W'일 때 칠해야 하는 횟수
        
        # 현재 좌표 (i, j)부터 시작해 8x8범위 탐색
        # (행, 열) = (a, b) 좌표
        for a in range(i, i+8):
            for b in range(j, j+8):
		            # a+b가 짝수
                if (a+b) % 2 ==0:
                    if board[a][b] != 'B':
                        is_black += 1 # B로 시작할 때는 여기가 B여야 함
                    if board[a][b] != 'W':
                        is_white += 1 # W로 시작할 때는 여기가 W여야 함
                else:
                    if board[a][b] != 'W':
                        is_black += 1
                    if board[a][b] != 'B':
                        is_white += 1
        # B로 시작하는 경우, W로 시작하는 경우 중 최솟값 저장
        result.append(min(is_black, is_white))
# result 리스트에 있는 모든 8x8 체스판 중 가장 적게 칠한 값      
print(min(result))