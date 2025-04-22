import sys
input = sys.stdin.readline

k = int(input())
stack = []
for _ in range(k):
    stack.append(int(input()))
# [3, 0, 4, 0]
note = []
for i in stack:
    if i != 0:
        note.append(i)
    else:
        note.pop() # 가장 최근 값 빼기
    
print(sum(note))