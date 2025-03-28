import sys 
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    h, w, n = map(int,input().split())

    # 층수(y)
    y = n % h
    if y == 0:
        y = h

    # 호수(x)
    x = (n-1)//h + 1  

    print(f'{y}{x:02d}') # x는 두자리로 채울거고, 자릿수부족하면 0으로 채워줘      

# 101 ~ h0w, h0XX(w가 두자리 수)
#  yyxx
# 101 201 301 401 501 601 102 202 302 402 502 602
# 10 = 2*6-2= 2호이고,(6-2)층
# 72 = 3*30 -18 = 3호이고, (30-18)=12층 
# 즉, (n-1)//h +1 = xx호
# (n-1)인 이유는 n=6, h=6일때 => 601호자나?를 생각해보자 
# n % h == yy층
