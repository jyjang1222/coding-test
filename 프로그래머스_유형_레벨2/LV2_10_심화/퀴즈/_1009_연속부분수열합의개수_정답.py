# https://school.programmers.co.kr/learn/courses/30/lessons/131701
def solution(e):
    size = len(e)
    myset = set()
    n = 1
    mx = sum(e)
    myset.add(mx)
    halfsize= size // 2
    e = e * 2
    for i in range(halfsize):
        for j in range(size):               
            total = sum(e[j : j + n])
            myset.add(total)
            myset.add(mx - total)
        n += 1
    #print(myset)
    return len(myset)
elements = [7,9,1,1,4]
r = solution(elements)
print(r)