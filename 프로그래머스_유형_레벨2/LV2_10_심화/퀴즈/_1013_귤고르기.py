def solution(k, t):
    answer = 0
    di = {}
    for i in range(len(t)):
        if t[i] in di.keys():
            di[t[i]] += 1
        else:
            di[t[i]] = 1
    #print(di)
    sdict = sorted(di.items(), key=lambda x: x[1], reverse=True)
    #print(sdict)
    
    for i in range(len(sdict)):
        if k > 0:
            answer += 1
            k -= sdict[i][1]

    
    return answer


k , t = 10 , [1, 3, 2, 5, 4, 3 ,3 ,3 , 3, 3, 1, 1, 1, 1]
r = solution(k , t)
print(r)