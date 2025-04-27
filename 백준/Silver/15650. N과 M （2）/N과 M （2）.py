import sys
input = sys.stdin.readline


n, m = map(int, input().split(' '))

# 조합 => 순서가 상관없어 : (1,2,3) == (3,2,1)
def dfs(start, n, m, buf):
    # 길이가 m 일때 출력
    if len(buf) == m:
        print(*buf) # 원소만 
    for i in range(start, n+1):
        # 숫자 중복은 안돼
        if i not in buf:
            buf.append(i)
            # print(buf)
            # 순서가 상관없어서 i부터 시작
            dfs(i, n, m, buf)
            buf.pop()
            # print(buf)

dfs(1,n,m,[])   