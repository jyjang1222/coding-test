# https://school.programmers.co.kr/learn/courses/30/lessons/42839

import math
def printArr(arr , r):
    for i in range(r):
        print(arr[i] , end=" ")
    print()
    print("--------------------")
def getPerm(st , r):
    #print(st)
    arr =[]
    for i in range(len(st)):
        arr.append(st[i])
    node = {"d" : 0 , "arr" : arr}
    stack = []
    mx = len(st)
    stack.append(node)
    myset = set()
    while True:
        if len(stack) == 0:
            break
        pop = stack.pop()
        d = pop["d"]
        arr = pop["arr"]
        if d == r:
            st = ""
            for i in range(r):
                st += arr[i]
            myset.add(int(st))
            continue
        for i in range(d , mx):
            temp = []
            for j in range(len(arr)):
                temp.append(arr[j])
            
            swap = temp[i]
            temp[i] = temp[d]
            temp[d] = swap
            node = {"d" : d + 1 , "arr" : temp}
            stack.append(node)
    return myset

def getPrimeNumber(num):
    if num <= 1:
        return False
    sqrt = math.sqrt(num)
    for i in range(2, int(sqrt) + 1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    myset = set()
    for i in range(len(numbers)):
        r = i + 1        
        a = getPerm(numbers , r)
        myset.update(a)
    print(myset)
    for v in myset:
        if getPrimeNumber(v):
            answer += 1
    
    return answer

numbers = "011"
r = solution(numbers)
print(r)