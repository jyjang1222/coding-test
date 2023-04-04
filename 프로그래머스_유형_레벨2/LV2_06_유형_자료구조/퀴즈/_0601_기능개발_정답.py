# https://school.programmers.co.kr/learn/courses/30/lessons/42586

def check100(p , s):
    c = 0
    while True:
        #print(p , s)
        if len(p) == 0:
            break
        if p[0] == 100 :
            del(p[0])
            del(s[0])
            c += 1
        else:
            break
    return c
def solution(p, s):
    arr = []
    size = len(p)
    c = 0
    while True:
        if c == size:
            break
        for i in range(len(p)):
            count = check100(p , s)
            c += count
            if count > 0:
                arr.append(count)
        for i in range(len(p)):
            p[i] += s[i]
            if p[i] >= 100:
                p[i] = 100     
    return arr

p = [93,30,50]
s = [1,30,5]
r = solution(p, s)
print(r)
