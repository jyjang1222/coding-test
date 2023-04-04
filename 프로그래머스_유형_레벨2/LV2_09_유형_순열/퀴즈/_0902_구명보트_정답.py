# https://school.programmers.co.kr/learn/courses/30/lessons/42885

def solution(p, limit):
    c = 0
    p.sort()
    p.reverse()
    start = 0
    end = len(p) - 1
    print(p)
    while True: 
        if start > end:
            return c
        if start == end:
            return c + 1
        c += 1
        total = 0
        while total + p[start] <= limit:      
            total += p[start]
            start += 1
        if start > end:
            return c
        if start == end:
            return c + 1

        while total + p[end] <= limit:            
            total += p[end]
            end -= 1
            

people = [70, 80, 50]
limit = 100
r = solution(people , limit)
print(r)





