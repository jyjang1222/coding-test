# https://school.programmers.co.kr/learn/courses/30/lessons/42587

def solution(p, l):
    c = 1
    mx = max(p)
    #print(p, l)
    while True:
        
        if p[0] == mx and l == 0:
            break
        if p[0] == mx:
            del(p[0])
            mx = max(p)
            c += 1

        else:
            temp = p[0]
            p = p[1:]
            p.append(temp)
            
        l -= 1
        if l < 0:
            l = len(p) - 1
        #print(p , l)
    return c

p = [1, 1, 9, 1, 1, 1]
l = 0
r = solution(p , l)
print(r)

"""
큐의 원리를 이용한다.

"""