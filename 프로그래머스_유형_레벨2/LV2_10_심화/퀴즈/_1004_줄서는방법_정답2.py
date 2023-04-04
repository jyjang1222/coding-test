# https://school.programmers.co.kr/learn/courses/30/lessons/12936

# https://dev-dain.tistory.com/205

import math

def solution(n, k):
    answer = []
    arr = [x for x in range(1, n + 1)]
    k -= 1

    while True:
        if n == 0:
            break
        fnum = math.factorial(n)
        share = fnum // n
        index = k // share
        answer.append(arr[index])
        arr.pop(index)
        k %= share
        n -= 1

    return answer

n = 3
k = 5
r = solution(n , k)
print(r)