# https://school.programmers.co.kr/learn/courses/30/lessons/42577

def solution(p):
    p.sort()
    #print(p)
    
    for i in range(len(p) - 1):
        a = p[i]
        b = p[i + 1]
        if len(b) < len(a):
            continue
        c = b[:len(a)]
        if a == c:
            return False 
        pass
    return True
    pass

p = ["123", "456", "789"]
r = solution(p)
print(r)
