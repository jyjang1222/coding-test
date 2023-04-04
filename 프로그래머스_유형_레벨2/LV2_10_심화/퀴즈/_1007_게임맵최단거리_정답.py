# https://school.programmers.co.kr/learn/courses/30/lessons/1844


class Node:
    x = 0
    y = 0
def solution(maps):
    answer = 1
    ey = len(maps)
    ex = len(maps[0])
    check = []
    for i in range(ey):
        check.append([0 for j in range(ex)])
    node = Node()
    node.x = 0
    node.y = 0
    check[0][0] = 1
    stack = [node]
    while True:
        if len(stack) == 0:
            return -1 
        answer += 1
        ylist = [0,0,-1,1]
        xlist = [-1,1,0,0]
        popstack = stack # 중요한부분 
        stack = []
        for i in range(len(popstack)):
            pop = popstack[i]
            x = pop.x
            y = pop.y
            for j in range(4):
                nx = x + xlist[j]
                ny = y + ylist[j]
                if nx < 0 or ny < 0 or nx >= ex or ny >= ey:
                    continue
                if nx == ex - 1 and ny == ey - 1:
                    return answer
                if check[ny][nx] == 0 and maps[ny][nx] == 1:
                    check[ny][nx] = 1
                    node = Node()
                    node.x = nx
                    node.y = ny
                    stack.append(node)      

        
maps = [[1,0,1,1,1],
        [1,0,1,0,1],
        [1,0,1,1,1],
        [1,1,1,0,1],
        [0,0,0,0,1]]

r = solution(maps)
print(r)