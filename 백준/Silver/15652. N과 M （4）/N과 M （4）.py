import sys
input = sys.stdin.readline
n, m = map(int, input().split())
# sys.setrecursionlimit(3000) # 예시: 재귀 깊이 제한을 높임

# 중복 조합 => 순서는 상관없지만 중복가능 : (1,2,1) == (2,1,1)
def dfs(start, n, m, buf):
    # 길이가 m 일때 출력
    if len(buf) == m:
        print(*buf) # 원소만
        return
    for i in range(start, n+1):
        # 숫자 중복 가능하니까 if문 필요 없지
        # if i not in buf:
        buf.append(i)
        # print(buf)
        # 순서가 상관없어서 i부터 시작 => 조합
        dfs(i, n, m, buf)
        buf.pop()
        # print(buf)

dfs(1,n,m,[])   