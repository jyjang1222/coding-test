
def factorial_loop(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial_recurssion(n):
    if n <= 1:
        return 1
    
    return n * factorial_recurssion(n-1)

a = factorial_loop(5)
print(a)
b = factorial_recurssion(5)
print(b)
