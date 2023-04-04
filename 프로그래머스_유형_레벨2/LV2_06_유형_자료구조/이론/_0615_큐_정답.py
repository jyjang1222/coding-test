
"""
    q배열에 전부 1씩 더한다.
    한번 1씩 더할때마다 카운트가 0부터 증가한다. 
    q배열에 값이 100이되면 더이상 증가하지않는다. 
    100 이완료되면 q배열의 값은 삭제된다. 
    time 배열은 q배열의 값이 삭제될때의 count를 저장한다.
    단, q배열은 맨앞의 값이 100이 안되면,
    뒤의 값이 100이라도 삭제될수없다.

    time = [11, 70, 70] 
"""
q = [89,30,50]
time = []
c = 0
while True:
    if len(q) == 0:
        break

    if q[0] == 100:
        time.append(c)
        del(q[0])
    else:
        for i in range(len(q)):
            q[i] += 1
            if q[i] >= 100:
                q[i] = 100
        c += 1
print(time)
