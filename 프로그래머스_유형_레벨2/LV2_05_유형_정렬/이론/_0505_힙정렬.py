

def heap_sort(a):
    # 최대 힙 만들기 (가장큰값이 맨위로 오게한다.)
    size = len(a)
    for i in range(1, size):
        c = i
        while c != 0:
            p = (c - 1) // 2 
            if a[p] < a[c]:
                temp = a[p]
                a[p] = a[c]
                a[c] = temp
            c = p
    #print(a)

    # 정렬시작
    last = len(a) - 1
    for i in range(len(a)):
        #print(last)
        temp = a[last]
        a[last] = a[0]
        a[0] = temp

        p = 0
        c = 1

        while c < last:
            c = p * 2 + 1
            # 자식 두개중 큰값을 찾는다.
            if c < last-1 and a[c] < a[c + 1]:
                c += 1

            if c < last and a[p] < a[c]:
                temp = a[p]
                a[p] = a[c]
                a[c] = temp
            p = c
        last -= 1
    
    return a


a = [54,88,77,26,93,67,8,98,6,4] 
print(a)
a = heap_sort(a)
print(a)