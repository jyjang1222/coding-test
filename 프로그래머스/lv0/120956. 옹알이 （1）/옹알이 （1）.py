def solution(babbling):
    arr = ['aya', 'ye', 'woo', 'ma']
    arr2 = ['aya', 'ye', 'woo', 'ma']
    cnt = 0
    
    # 조합2
    for i in arr:
        for j in arr:
            if i != j:
                tmp = i + j
                arr2.append(tmp)
                tmp = ''
    # 조합3
    for i in arr:
        for j in arr:
            for k in arr:
                if i != j and i != k and j != k:
                    tmp = i + j + k
                    arr2.append(tmp)
                    tmp = ''
    # 조합4        
    for i in arr:
        for j in arr:
            for k in arr:
                for m in arr:
                    if i != j and i != k and i != m and j != k and j != m and k != m:
                        tmp = i + j + k + m
                        arr2.append(tmp)
                        tmp = ''
                
            
    for i in arr2:
        for j in babbling:
            if i == j:
                cnt += 1
    answer = cnt
    print(arr2)
    return answer