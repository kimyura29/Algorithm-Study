from collections import deque
# 한 글자만 다른 단언지 확인하는 함수
def can_change(word1, word2):
    count = 0
    for a, b in zip(word1, word2):
        if a != b:
            count += 1
        if count > 1:
            return 0
    return 1

def solution(begin, target, words):
    answer = 0
    # words에 target이 있는지 확인
    if target not in words:
        return 0
    visit = set() # 방문 처리
    queue = deque()
    queue.append((begin,0)) # 시작 단어, 변환수
    # 한 알파벳만 변경 가능한데, words안에 있는 단어만 가능
    while queue:
        cx, cnt = queue.popleft()
        if cx == target:
            return cnt
        for nx in words:
            # can_change가 1이고, 아직 방문 안했으면
            if can_change(cx, nx) and nx not in visit:
                queue.append((nx, cnt+1))
                visit.add(nx)
        
    return cnt