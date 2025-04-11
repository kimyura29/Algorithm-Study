import sys
input = sys.stdin.readline


# 입력: ( [ ] )       → 스택: ( → ([ → ( [ ] → ( → 빈 → ✅
# 입력: ( [ ) ]       → 스택: ( → ([ → 틀린 괄호 짝 → ❌
# 입력: ( ( [ ] ) )   → 스택: ( ( [ → ( ( → ( → 빈 → ✅
# 입력: ( [           → 스택: ( → ([ → 아직 닫는 괄호 없음 → ❌
# 균형 검사 (스택 => 선입후출)
def balanced(x):
    stack = []
    # 문자열 검사 시작
    for i in x:
        # 1. 여는 괄호 나오면 스택에 넣음
        if i in '([':
            stack.append(i)
        # 2. 닫는 소괄호 ')'일 때
        elif i == ')':
            # 스택이 비어있거나, 가장 최근에 들어온 값이 '('이 아니면 잘못된 짝
            if (len(stack) == 0) or stack[-1] != '(':
                return False
            stack.pop()
         # 3. 닫는 대괄호 ']'일 때
        elif i == ']':
            if not stack or stack[-1] != '[':
                return False
            stack.pop()
    # 마지막에 스택이 비어있으면 균형이 맞은 것
    return not stack  


# 입력 받기
while True:
    string =  input().rstrip() # 오른쪽 공백만 제거 => 줄마다 평가
    if string == '.':
        break

    # 균형 검사 실행 후 결과 출력
    if balanced(string):
        print("yes")
    else:
        print("no")
