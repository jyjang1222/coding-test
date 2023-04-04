# https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    stack = []
    for i in range(len(s)):
        a = s[i]
        if a == "(":
            stack.append(a)          
        elif a == ")":
            if len(stack) == 0:
                return False
            peek = stack[-1]
            if peek == "(":
                stack.pop()
            elif peek == ")":
                return False
    if len(stack) > 0 : 
        return False
    else:
        return True
s = "()())"
r = solution(s)
print(r)

