
def heap_print(a):
    for i in range(1, len(a)):
        c = i
        print(a[c] , end=" : ")
        while c != 0:
            p = (c - 1) // 2
            print(a[p] , end=" ")
            c = p
        print()
    pass
a = ["a","b","c","d","e","f","g","h","i","j","k","l"]

"""
    위 배열을 트리 구조로 만들면 다음과같다.
    각각의 값들의 모든 부모를 출력해보자.
                   a
            b               c
        d      e        f       g
    h     i  j   k   l
"""
heap_print(a)
