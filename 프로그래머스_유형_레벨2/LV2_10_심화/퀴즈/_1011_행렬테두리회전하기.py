def getArr(r , c):
    k = 1
    arr = []
    for i in range(r):
        arr.append([])
        for j in range(c):
            arr[i].append(k)
            k += 1
    return arr

def printArr(arr):
    for i in range(len(arr)):
        print(arr[i])
    print("------------------------")

def solution(r, c, q):
    arr = getArr(r , c)
    answer = []
    for v in q:
        #printArr(arr)    
        sy1 , sy2 = v[0] - 1 , v[0] - 1
        sx1 , sx2 = v[1] - 1 , v[1] - 1
        ey1 , ey2 = v[2] - 1 , v[2] - 1
        ex1 , ex2 = v[3] - 1 , v[3] - 1
        
        temp = []
        for i in range(sx1 , ex1):
            temp.append(arr[sy2][sx2])      
            sx2 += 1         
        for i in range(sy1 , ey1):
            temp.append(arr[sy2][sx2])      
            sy2 += 1      
        for i in range(sx1 , ex1):
            temp.append(arr[sy2][sx2])      
            sx2 -= 1
        for i in range(sy1 , ey1):
            temp.append(arr[sy2][sx2])      
            sy2 -= 1

        last = temp[-1]
        temp.insert(0 , last)
        temp.pop()
        answer.append(min(temp))

        sy1 , sy2 = v[0] - 1 , v[0] - 1
        sx1 , sx2 = v[1] - 1 , v[1] - 1
        ey1 , ey2 = v[2] - 1 , v[2] - 1
        ex1 , ex2 = v[3] - 1 , v[3] - 1

        k =0
        for i in range(sx1 , ex1):
            arr[sy2][sx2] = temp[k]
            k += 1
            sx2 += 1   
        for i in range(sy1 , ey1):
            arr[sy2][sx2] = temp[k]
            k += 1
            sy2 += 1    
        for i in range(sx1 , ex1):
            arr[sy2][sx2] = temp[k]
            k += 1
            sx2 -= 1
        for i in range(sy1 , ey1):
            arr[sy2][sx2] = temp[k]
            k += 1
            sy2 -= 1
        #printArr(arr)    
    return answer

r = 6
c = 6
q = [
    [2,2,5,4],
    [3,3,6,6],
    [5,1,6,3]]
result = solution(r, c, q)
print(result)