# https://school.programmers.co.kr/learn/courses/30/lessons/12946

# 하노이의 탑
def solution(n):
    answer = []
    
    def hanoi(src, tgt, inter, n): 
        if n == 1:
            answer.append([src, tgt])
        else:
            hanoi(src,inter,tgt,n-1)
            hanoi(src,tgt,inter,1)
            hanoi(inter,tgt,src,n-1)
            
    hanoi(1,3,2,n)
    return answer

n = 2
r = solution(n)
print(r)
