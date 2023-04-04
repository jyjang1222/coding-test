# https://school.programmers.co.kr/learn/courses/30/lessons/12936

def getArr(n):
    arr = []
    for i in range(n):
        arr.append(i + 1)
    return arr

def solution(n, k):
    answer = []
    result = []
    arr = getArr(n)
    stack = []
    node = {"arr" : arr , "d" : 0}
    stack.append(node)
    while True:
        if len(stack) == 0:
            break
        pop = stack.pop(0)
        d = pop["d"]
        arr = pop["arr"]
        if d == n:
            a = "".join(map(str, arr))
            result.append(a)       
            continue      
        for j in  range(d , n):
            tempArr = arr.copy()
            temp = tempArr[j]
            tempArr[j] = tempArr[d]
            tempArr[d] = temp
            node = {"arr" : tempArr , "d" : d + 1}
            stack.append(node)
    result.sort()
    #print(result)
    a = result[k-1]
    answer = list(map(int, a))
    return answer

n = 3
k = 5
r = solution(n , k)
print(r)