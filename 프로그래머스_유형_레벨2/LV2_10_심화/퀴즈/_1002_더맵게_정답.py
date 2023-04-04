# https://school.programmers.co.kr/learn/courses/30/lessons/42626

import heapq

def solution(s, k):
    answer = 0
    heapq.heapify(s)
    while True:
        m = s[0]
        if m >= k:
            break
        if len(s) <= 1:
            return -1
        

        a = heapq.heappop(s)
        b = heapq.heappop(s)
        c = a + (b * 2)
        heapq.heappush(s , c)
        answer += 1
    return answer


s = [1, 1]	
K = 3
r = solution(s, K)
print(r)