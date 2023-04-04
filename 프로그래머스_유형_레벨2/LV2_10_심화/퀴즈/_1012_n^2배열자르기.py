# https://school.programmers.co.kr/learn/courses/30/lessons/87390



def solution(n, left, right):
    k = left % n + 1
    o = left // n + 1
    arr = []
    for i in range(left, right + 1):
        if o >= k:
            #print(o , end="")  
            arr.append(o)
        else:
            #print(k , end="")   
            arr.append(k)        
        # if o >= k :
        #     a = 0
        # elif o < k:
        #     print(o + k, end="" )       
        if i % n == n - 1:
            k = 1
            o += 1
            print()
        else:
            k += 1
    return arr
n = 3
left = 2
right = 5
r = solution(n , left , right)
print(r)
