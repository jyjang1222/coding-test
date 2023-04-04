# https://school.programmers.co.kr/learn/courses/30/lessons/76502

def checkBracket(s):
    if len(s) % 2 == 1:
        return False
    stack = []
    stack.append(s[0])
    i = 1
    while True:
        if i == len(s):
            break
        b = s[i]
        if len(stack) == 0:
            stack.append(b)
        else:
            pop = stack[-1]
            if b in "{([":
                stack.append(b)
            elif b == "]"  and pop == "[":
                stack.pop()
            elif b == "}"  and pop == "{":
                stack.pop()
            elif b == ")"  and pop == "(":
                stack.pop()    
        i += 1
    if len(stack) > 0:
        return False
    return True
def solution(s):
    answer = 0
    size = len(s)
    for i in range(size):
        if checkBracket(s):
            answer += 1
        # print(s , " " , answer)
        a = s[0]
        s = s[1:]
        s += a
    return answer
s = "}]()[{"

r = solution(s)
print(r)