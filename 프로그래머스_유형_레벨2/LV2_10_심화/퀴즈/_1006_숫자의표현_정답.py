# https://school.programmers.co.kr/learn/courses/30/lessons/12924

def solution(n):
    answer = 1
    b = 1
    e = 1
    total = 0
    while True:
        
        if total < n:
            total += e
            e += 1
        elif total > n:
            total -= b
            b += 1
        elif total == n:
            #print(b , e , n , total)
            answer += 1
            total += e
            e += 1
        if b >= n:
            break
    
    return answer

n = 15
r = solution(n)
print(r)