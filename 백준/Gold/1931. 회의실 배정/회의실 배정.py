import sys
input = sys.stdin.readline
n = int(input())

time_table = []
for _ in range(n):
    s, e = map(int,input().split())
    time_table.append((s,e))

# 최대 회의 수 계산
# 끝나는 시간 e를 먼저 오름차순, 같다면 s가 작은순 정렬
time_table.sort(key = lambda x: (x[1], x[0])) # e를 기준으로 정렬하고, e가 같다면 s로 정렬

# 그리디
end_time = 0 # 현재 회의 끝난 시간
count = 0 # 총 회의 수

for s, e in time_table:
    if s >= end_time:
        count += 1
        end_time = e # 다음 회의 시작 시간 조건
print(count)