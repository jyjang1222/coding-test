# https://school.programmers.co.kr/learn/courses/30/lessons/84512

def perm( mx):
    di = "AEIOU"
    node = {"c" : 0 , "arr" : "" }
    stack =[]
    stack.append(node)
    mylist = []
    while True:
        if len(stack) == 0:
            break
        pop = stack.pop()
        c = pop["c"]
        arr = pop["arr"]
        if c == mx:
            mylist.append(arr)
            continue   
        for i in range(len(di)):
            node = {"c" : c , "arr" : arr}
            node["c"] += 1
            node["arr"] += di[i]
            stack.append(node)
    return mylist
def solution(word):
    answer = 0
    a = []
    for i in range(5):   
        a += perm(i + 1)
    #print(a)
    a.sort()
    for i in range(len(a)):
        if word == a[i]:
            return i + 1
    return -1


word = "AAAAE"
r = solution(word)
print(r)