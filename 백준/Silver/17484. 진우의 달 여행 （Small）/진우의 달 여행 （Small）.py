import sys
input = sys.stdin.readline

n, m = map(int, input().split())
fuel = [list(map(int, input().split())) for _ in range(n)] # 2차원 배열 => n행 X m열

# 최소 연료량이니까 무한대로 dp 저장
# 우주선 방향 [0]아래 왼쪽 대각선, [1]아래, [2]아래 오른쪽 대각선 방향 각각 연료량 저장
dp = [[[float('inf')] * 3 for _ in range(m)] for _ in range(n)] # 3차원 배열(방향)

# maps[0][i] -> map[5][j] 이렇게 가야 해 (i,j는 0~(m-1)사이의 값)
# 시작 지점 
for j in range(m): # 열
    for k in range(3): # 방향
        dp[0][j][k] = fuel[0][j]

# dp 테이블 채우기
for i in range(1,n): # 행
    for j in range(m): # 열
        for k in range(3): # 방향(0:왼대, 1:아래, 2:오대)
            for prev_k in range(3): # 이전 방향
                # 방향이 두번 연속 x
                if k == prev_k:
                    continue # 건너뛰기
                # 이전 열의 위치 (방향(0:왼대, 1:아래, 2:오대)을 생각해)
                next_j = j + k - 1
                # 경계값 계산
                if 0 <= next_j < m:
                    # i행 j열에 k 방향으로 왔을 때 연료
                    dp[i][j][k] = min(dp[i][j][k], dp[i-1][next_j][prev_k]+fuel[i][j])

result = float('inf')
for j in range(m):
    for k in range(3):
        result = min(dp[n-1][j][k], result)

print(result)