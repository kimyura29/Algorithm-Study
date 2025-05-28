import sys
from collections import defaultdict 
input = sys.stdin.readline

m = int(input())
cocktail = defaultdict(int)
for _ in range(m):
    s,x = input().split()
    cocktail[s] += int(x)

# {'Cola': 242, 'Vodka': 150}
# print(cocktail)
c_value = list(cocktail.values())
# print(c_value) # [242, 150]
gold = False
for i in range(len(c_value)):
    for j in range(len(c_value)):
        if i != j:
            if int(c_value[i] * 1.618) == c_value[j]:
                gold = True
                break
    if gold:
        break
print('Delicious!' if gold else 'Not Delicious...')