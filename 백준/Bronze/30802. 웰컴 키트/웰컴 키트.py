import sys 
input = sys.stdin.readline

n = int(input())
s,m,l,xl,xxl,xxxl = map(int, input().split())
t, p = map(int,input().split())

sizes = [s,m,l,xl,xxl,xxxl]
tshirts = 0
for size in sizes:
    if size % t == 0:
        tshirt = (size // t)
    else:
        tshirt = (size // t + 1)
    tshirts += tshirt

print(tshirts)
print(n//p, n%p)