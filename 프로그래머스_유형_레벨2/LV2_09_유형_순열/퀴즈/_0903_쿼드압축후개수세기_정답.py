
def solution(arr):
    answer = []
    node = {"size" : len(arr), "index" : 0, "y" : 0 , "x" :  0}
    stack =[node]
    while True:
        if len(stack) == 0:
            break
        pop = stack.pop(0)
        size = pop["size"]
        index = pop["index"]
        y = pop["y"]
        x = pop["x"]
        if size == 0:
            print(pop)
            continue    
        halfx = size//2
        halfy = size//2
        xlist = [x, x + halfx , x , x + halfx]
        ylist = [y, y , y + halfy , y + halfy]
        for i in range(4):
            node = {"size" : size//2, "index" : i, "y" : ylist[i] , "x" :  xlist[i]}
            stack.append(node)

    return answer


arr = [
    [1,1,1,1,1,1,1,1],
    [0,1,1,1,1,1,1,1],
    [0,0,0,0,1,1,1,1],
    [0,1,0,0,1,1,1,1],
    [0,0,0,0,0,0,1,1],
    [0,0,0,0,0,0,0,1],
    [0,0,0,0,1,0,0,1],
    [0,0,0,0,1,1,1,1]]

arr = [
    [1,1,0,0],
    [1,0,0,0],
    [1,0,0,1],
    [1,1,1,1]]

r = solution(arr)
print(r)