import sys
input = sys.stdin.readline

n,r,c = map(int, input().split())


# 재귀 함수 설계 => 문제를 계속해서 더 작은 사각형으로 쪼갬(재귀)
def z(n,r,c):
    # 종료조건 n=1이 되면 직접 계산
    if n == 1:
        return 2 * r + c
    # 격자 분할 기준
    half = 2 ** (n-1)
    size = half * half
    # 전체 사각형 기준 r이 행, c가 열
    # 1사분면
    if r < half and c < half:
        return 0 * size + z(n-1, r, c)
    # 2사분면
    elif r < half and c >= half:
        return 1 * size + z(n-1, r, c-half) # 1사 기준으로 r(행)은 half 상측으로 같은데 c(열)은 half 우측에 위치해서 
    # 3사분면
    elif r >= half and c < half:
        return 2 * size + z(n-1, r-half, c) # 1사 기준으로 r(행)은 half 하측으로 반대라서
    # 4사분면
    elif r >= half and c >= half:
        return 3 * size + z(n-1, r-half, c-half)  # 1사 기준으로 r(행)이 half 하측으로 반대, c(열)도 half 우측으로 반대   


print(z(n,r,c))
