# https://daimhada.tistory.com/107

from collections import deque

dq = deque([])

dq.append(10)
dq.append(20)
dq.append(30)
dq.append(40)
dq.append(50)

print(dq)

print(dq.popleft())
print(dq.popleft())
print(dq)
