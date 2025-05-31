import sys
sys.setrecursionlimit(10**6) # 재귀 제한 해제

# 여러줄 입력되는데 몇 줄인지 모름
pre_order = []
for line in sys.stdin:
    pre_order.append(int(line.strip()))

idx = 0 # 현재 탐색 중인 노드 인덱스

# 이진 탐색 트리를 전위 순회 결과로부터 재귀적으로 복원하며 후위 순회 결과를 만들어내는 함수
def sol(min_val, max_val):
    global idx
    if idx >= len(pre_order): # 모든 노드를 다 봤으면 종료
        return []

    curr = pre_order[idx]  # 현재 노드 값
    # 현재 값이 [min_val, max_val] 범위를 벗어나면 현재 서브트리에 들어갈 수 없는 값이므로 return
    if not (min_val < curr < max_val):
        return []

    idx += 1  # 현재 노드 사용했으니 인덱스 증가

    # 왼쪽 서브트리: 값이 curr보다 작아야 함 → (min_val, curr) 범위
    left = sol(min_val, curr)
    # 오른쪽 서브트리: 값이 curr보다 커야 함 → (curr, max_val) 범위
    right = sol(curr, max_val)

    # 후위 순회: 왼쪽 → 오른쪽 → 루트 순서로 리스트 반환
    return left + right + [curr]  # 후위 순회: 왼→오→루트

# 트리 전체를 처리 (루트의 범위는 무한대)
result = sol(-float('inf'), float('inf'))
for r in result:
    print(r)