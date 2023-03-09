def solution(x):
    answer = False
    total = 0
    n = x
    while n != 0:
        total += n % 10
        n //= 10
    if x % total == 0:
        answer = True
    return answer
