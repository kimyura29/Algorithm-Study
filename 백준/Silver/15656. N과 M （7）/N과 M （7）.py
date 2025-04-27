import sys
input = sys.stdin.readline
n, m = map(int, input().split())
permutation = sorted(list(map(int, input().split()))) # 사전 순으로 증가하는 순서


# 중복 순열
def dfs(n, m, buf):
    # 길이가 m인 수열
    if len(buf) == m:
        print(*buf) # 원소만 출력
        return # 필수
        
    for i in permutation:
        # buf가 빈 리스트로 시작
        buf.append(i)

        dfs(n, m, buf)
        buf.pop()


dfs(n, m, [])