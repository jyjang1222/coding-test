# https://school.programmers.co.kr/learn/courses/30/lessons/42578

def solution(c):
    d = {}
    for v in c:
        kind = v[1]
        if kind in d:
            d[kind] += 1
        else:
            d[kind] = 1
    print(d)
    total = 1
    for i in d.keys():
        a = d[i] + 1
        total *= a
        
    
    return total - 1

c = [["yellow_hat", "headgear"], 
     ["blue_sunglasses", "eyewear"], 
     ["green_turban", "headgear"]]
r = solution(c)
print(r)