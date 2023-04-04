# https://school.programmers.co.kr/learn/courses/30/lessons/12973

def solution(s):
    if s == "":
        return 1
    if len(s) <= 1:
        return 0
    arr = []
    arr.append(s[0])
    i = 1
    while True:
        if i >= len(s):
            break
        if len(arr) == 0:
            arr.append(s[i])
            i += 1
            continue
        a = arr[-1]
        b = s[i]
        if a == b:
            arr.pop()
        else:
            arr.append(s[i])
        i += 1

    if len(arr) == 0:
        return 1
    
    return 0

s = "baabaa"
r = solution(s)
print(r)