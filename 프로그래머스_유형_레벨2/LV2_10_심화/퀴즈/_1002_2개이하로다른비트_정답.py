# https://school.programmers.co.kr/learn/courses/30/lessons/77885

def changeNumber(num):
    c = 1
    while True:
        if c >= num:
            break
        c *= 2
        
    st = ""
    while True:
        a = num // c
        num = num % c
        st += str(a)
        c //= 2  
        if c == 0:
            break
    return st
    
def changeBit(bit):
    c = 1
    a = 0
    for i in range(len(bit)):
        a += int(bit[-(i + 1)]) * c
        c *= 2
    return a
    pass

def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        num = numbers[i]
        a = changeNumber(numbers[i])
        a = "0" + a
        if num % 2 == 0:
            a = a[:-1] + "1"
            c = changeBit(a)
            answer.append(c)
            pass
        else:
            last = len(a) - 1
            for i in range(len(a)):
                if a[last] == "0":
                    a = a[:last] + "10" + a[last+2:]
                    c = changeBit(a)
                    answer.append(c)
                    break
                last -= 1
    
    return answer

n = [2,7]
r = solution(n)
print(r)


"""
[전용알고리즘이다]
    [1단계] 
        숫자가 짝수인 경우, 항상 가장 마지막 비트는 0이다.
        따라서 마지막 비트를 0에서 1로 바꿔준 값이 답이기 때문에 숫자+1 값을 answer에 넣어준다.
        숫자가 홀수인 경우,
        가장 뒤쪽에 있는 0을 1로 바꿔주고 그다음 비트를 0으로 바꿔주면 된다.
        예를 들어 7(0111) 은 가장 뒤쪽에 있는 0을 1로 바꿔주고 그다음 비트를 0으로 바꿔준다. 
        즉, 11(1011)이 답이다.
        그리고 9(1001) 은 1001 -> 1011 -> 1010 으로 10이 답이다.
    [2단계] 
        이진법을 십진법으로 바꿔준다. 

"""