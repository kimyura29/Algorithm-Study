import sys
input = sys.stdin.readline
n = int(input())
S = input()
result = ""

for s in S:
    if s == "I":
        result += "i"
    elif s == "l":
        result += "L"

print(result)