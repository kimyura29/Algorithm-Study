import sys
input = sys.stdin.readline
n, m = map(int, input().split())


# 중복 순열
def dfs(start, n, m, buf):
    # 길이가 m인 수열
    if len(buf) == m:
        print(*buf) # 원소만 출력
        return
        
    for i in range(start, n+1):
        # buf가 빈 리스트로 시작
        # 중복이 가능하니까 확인할 필요 없어
        # if i not in buf: # buf = [ ]
        buf.append(i)
        # print(buf)
        # 다시 s=1부터 => 순서가 상관없으니까
        dfs(start, n, m, buf)
        buf.pop()
        # print(buf)

dfs(1, n, m, [])

