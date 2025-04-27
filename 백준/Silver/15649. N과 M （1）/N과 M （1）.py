import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# 순열
def dfs(start, n, m, buf):
    # 길이가 m인 수열
    if len(buf) == m:
        print(*buf) # 원소만 출력
    for i in range(start, n+1):
        # buf가 빈 리스트로 시작
        # buf에 i가 없다면
        if i not in buf: # buf = [ ]
            buf.append(i)
            # print(buf)
            # 다시 start=1부터 
            dfs(start, n, m, buf)

            buf.pop()
            # print(buf)

dfs(1, n, m, [])
