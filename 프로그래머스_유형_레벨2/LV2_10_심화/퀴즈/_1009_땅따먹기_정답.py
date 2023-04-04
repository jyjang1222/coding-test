# https://school.programmers.co.kr/learn/courses/30/lessons/12913

def solution(land):
    answer = 0  

    for i in range(1, len(land)):
        frontArr = land[i-1]
        for j in range(len(land[i])):
            mx = 0
            for k in range(len(frontArr)):
                if j != k and mx < frontArr[k]:
                    mx = frontArr[k]
            land[i][j] += mx
    # print(land)
    answer = max(land[-1]) 
    return answer


land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
r = solution(land)
print(r)