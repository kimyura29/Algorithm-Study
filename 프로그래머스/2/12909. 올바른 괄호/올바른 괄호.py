def solution(s):
    answer = True
    stack=[]
    for i in s:
        if i == '(':
            stack.append(i)
        elif i == ')':
            # 스택이 비어있거나 stack 마지막 들어온 값이 열린 괄호'('가 아니면
            if not stack or stack[-1] != '(':
                answer = False
                return answer
            if stack:
                stack.pop()
    if not stack:
        answer = True
    else:
        answer = False
    return answer