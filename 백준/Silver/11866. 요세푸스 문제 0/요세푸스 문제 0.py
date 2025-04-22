import sys
input = sys.stdin.readline

n, k = map(int, input().split())
people = []
for i in range(1, n+1):
    people.append(i)

idx = 0 # 시작
output = []
while people:
    idx = (idx + (k-1)) % len(people)
    removed = people.pop(idx) # idx
    output.append(removed)

print("<" + ", ".join(map(str, output)) + ">")