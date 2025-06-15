import sys
input = sys.stdin.readline
ip = input().strip()

if ip == 'M':
    print('MatKor')
elif ip == 'W':
    print('WiCys')
elif ip == 'C':
    print('CyKor')
elif ip == 'A':
    print('AlKor')
else:
    print('$clear')