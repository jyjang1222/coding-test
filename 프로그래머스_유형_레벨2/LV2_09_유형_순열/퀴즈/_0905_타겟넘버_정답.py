# https://school.programmers.co.kr/learn/courses/30/lessons/43165

def solution(num, target):
    d = {"index" : 0 , "total" : 0}
    stack = []
    stack.append(d)
    targetCount = 0
    size = len(num)
    while True:
        if len(stack) == 0:
            break
        pop = stack.pop()
        index = pop["index"]
        total = pop["total"]
        if index == size:
            if target == total:
                targetCount += 1
            continue
            pass
        val = num[index]
        
        t1 = {"index" : index + 1, "total" : total + val}       
        t2 = {"index" : index + 1, "total" : total - val}
        stack.append(t1)
        stack.append(t2)
    return targetCount


numbers	 = [1, 1, 1, 1, 1]	
target = 3

r = solution(numbers , target)
print(r)