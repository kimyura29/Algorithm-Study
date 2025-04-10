import sys
input = sys.stdin.readline

n = int(input())
member = []
for _ in range(n):
    age, name = input().split() # 자료형이 둘이 다르니까 map x
    member.append((int(age), name))

# 나이 기준으로 정렬 (나이가 같다면 입력순)
member.sort(key = lambda x: x[0])

for m in member:
    print(*m)

