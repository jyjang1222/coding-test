# https://inuplace.tistory.com/560

def getPowerSet(n,k):
    if n == k:
        return [[k]]

    basic = k        
    result = [[basic]]
    k += 1
    while (n >= k):
        for i in getPowerSet(n,k):
            result.append([basic] + i)
        k += 1

    return result

def powerSet(n) :
    result = []
    for i in range(1,n+1):
        result += getPowerSet(n,i)
    return result

n = 4
result = powerSet(n)

for line in result :
    print(line)
 