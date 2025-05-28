import sys
input = sys.stdin.readline
n,t = map(int, input().split())
bus_time = []
for _ in range(n):
    s,l,c = map(int,input().split())
    for i in range(c):
        if s + l * i >= t: # 런타임 에러 방지
            bus_time.append(s + l * i)
bus_time.sort() # 정렬

def solution(bus_time, t):
    time_list = []
    for i in bus_time:
        if i == t:
            return 0
        elif i > t:
            time_list.append(i-t)
    if time_list:
        return min(time_list)
    else:
        return -1

print(solution(bus_time, t))