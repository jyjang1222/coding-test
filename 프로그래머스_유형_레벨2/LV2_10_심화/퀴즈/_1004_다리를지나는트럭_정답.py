# https://school.programmers.co.kr/learn/courses/30/lessons/42583

from collections import deque

def solution(b, w, t):
    answer = 0
    test = [0 for i in range(b)]
    test = deque(test)
    t = deque(t)
    total = 0
    while True:
        #print(test)
        if len(test) == 0 and len(t) == 0:
            break
        total -= test[0]
        test.popleft()
        #del(test[0])
        a = 0
        b = 0
        c = 0 
        #if len(test) > 0:
        #    a = sum(test)
        if len(t) > 0:
            b = t[0]
        c = total + b
        if c <= w:
            if len(t) > 0:
                total += t[0]
                test.append(t[0])
                t.popleft()
        else:
            test.append(0)
        answer += 1
    return answer


b = 2
w = 10
t = [7,4,5,6]
r = solution(b , w , t)
print(r)