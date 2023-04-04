A, B, V = map(int, input().split())

def 달팽이(A, B, V):
    num = (V - A) // (A - B)
    if (V - A) % (A - B) == 0:
        num += 1
    else:
        num += 2

    return print(num)

달팽이(A, B, V)