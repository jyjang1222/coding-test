# https://school.programmers.co.kr/learn/courses/30/lessons/12980

def solution(n):
    ans = 0
    while True:
        if n == 0:
            break
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
            ans += 1
            n //= 2
    return ans

n = 5000
r = solution(n)
print(r)

"""
완전탐색을 할수도있지만 그러면 시간을 통과할수없다. 

도착점부터 출발점까지 오는걸로 계산해야한다.
짝수이면 2로 나누고, 홀수이면 1을빼주고 다시 2로 나눠준다. 
1을빼는과정에서 배터리가 소모된다. 

"""