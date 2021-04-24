# 이거도 다시 하자...
def solution(s):
    stack = []
    for bracket in s:
        if bracket == '(':
            stack.append(bracket)
        elif stack:
            stack.pop()
        else:
            return False
    return not stack
