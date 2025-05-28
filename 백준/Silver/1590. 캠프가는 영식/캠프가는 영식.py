import sys
input = sys.stdin.readline
n,t = map(int, input().split())
bus_time = []
for _ in range(n):
    s,l,c = map(int,input().split())
    for i in range(c):
        bus_time.append(s + l * i)

bus_time.sort() # 정렬

def sol(bus_time, t):
    left, right = 0, len(bus_time)-1 # 인덱스니까
    answer = float('inf') # 최소 시간 구하기

    while left <= right:
        mid = (left + right) // 2
        # 도착시간 = 버스시간 
        if bus_time[mid] == t:
            return 0
        elif bus_time[mid] > t:
            answer = min(answer, bus_time[mid])
            right = mid - 1
        else:
            left = mid + 1
    return answer - t if answer != float('inf') else -1 # 캠프에 갈 수 없으면 -1 출력
        

print(sol(bus_time, t))