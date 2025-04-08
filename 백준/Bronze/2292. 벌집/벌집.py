import sys
input = sys.stdin.readline

n = int(input())
room = 1 # 1번방에서 시작
floor = 1 # 1층에서 시작
while room < n:
    room += floor * 6
    floor += 1
print(floor)

