import sys
input = sys.stdin.readline

n,d = map(int,input().split())
road = [] # [[0, 50, 10], [0, 50, 20],..
for _ in range(n):
    s, f, l = map(int, input().split())
    # f가 총 도착지점인 d보다 작아야 의미있는 지름길
    if f <= d:
        road.append((s,f,l))
        
distance = [i for i in range(d+1)] # 고속도로 길이만큼

for i in range(d+1):
    if i != 0: # i가 0 이면 인덱스 오류
        distance[i] = min(distance[i], distance[i-1] + 1)
    for s, f, l in road:
        if s == i and distance[f] > distance[s] + l:
            distance[f] = distance[s] + l # 지름길로 갱신

print(distance[d])