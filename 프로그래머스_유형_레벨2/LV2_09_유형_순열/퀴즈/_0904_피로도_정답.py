# https://school.programmers.co.kr/learn/courses/30/lessons/87946

def getPerm(d):
    stack = []
    arr = d.copy()
    node = {"d": 0, "arr" : arr}
    size = len(d)
    stack.append(node)
    perm = []
    while True:
        if len(stack) == 0:
            break
        pop = stack.pop()
        d = pop["d"]
        arr = pop["arr"]
        if d == size:
            perm.append(arr)
            continue
        for i in range(d , size):
            temparr = arr.copy()
            
            temp = temparr[i]
            temparr[i] = temparr[d]
            temparr[d] = temp
            
            node = {"d" : d + 1 , "arr" : temparr}
            stack.append(node)
        pass
    return perm
    
def solution(k, d):
    answer = -1
    perm = getPerm(d)
    #print(perm)
    mx = 0
    for i in range(len(perm)):
        arr = perm[i]
        #print(arr)
        c = 0
        limit = k
        for j in range(len(arr)):         
            #print(arr[j][0] , end=" ")  
            if arr[j][0] <= limit:
                limit -= arr[j][1]
                c += 1
            else:
                break
        
        if c > mx:
            mx = c
        #print()
    return mx

k = 80
dungeons = 	[[80,20],[50,40],[30,10]]
r = solution(k , dungeons)
print(r)