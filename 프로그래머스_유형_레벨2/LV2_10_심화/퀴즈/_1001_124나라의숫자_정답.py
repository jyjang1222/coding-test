# https://school.programmers.co.kr/learn/courses/30/lessons/12899

# https://school.programmers.co.kr/learn/courses/30/lessons/12899

def solution(n):
    answer = ''
    temp = [4,1,2]
    while True:
        a = n % 3
        answer += str(temp[a])
        if a == 0:
            n -= 1
        n //= 3
        if n == 0:
            break
    a = list(answer)
    a.reverse()
    answer = ''.join(a)
    return answer
n = 6
r = solution(n)
print(r)