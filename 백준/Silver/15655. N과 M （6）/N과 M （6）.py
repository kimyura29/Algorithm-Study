import sys
input = sys.stdin.readline
n, m = map(int,input().split(' '))
comb = sorted(map(int, input().split())) # 사전순 정렬

# 조합
def dfs(start, buf):
    if len(buf) == m:
        print(*buf)
        return
    for idx in range(start, n):
        # 중복 안되니까
        if comb[idx] not in buf:
            buf.append(comb[idx])
            # 순서가 없어 => 조합이야
            dfs(idx, buf)
            buf.pop()

dfs(0, [])