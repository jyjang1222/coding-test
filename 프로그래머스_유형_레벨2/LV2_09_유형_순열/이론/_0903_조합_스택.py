# https://minhamina.tistory.com/38

class Node:
    depth = 0
    arr = ""

def combination(arr, n):
    result = []

    node = Node()
    stack = []
    stack.append(node)

    while True:
        if len(stack) == 0:
            break
        pop = stack.pop()
        if len(pop.arr) == n:
            print(pop.arr)
            continue
        
        if pop.depth == len(arr):
            continue

        temp = Node()
        temp.arr = pop.arr
        temp.depth = pop.depth + 1
        temp.arr += str(arr[pop.depth])
        
        stack.append(temp)

        temp = Node()
        temp.arr = pop.arr
        temp.depth = pop.depth + 1
        stack.append(temp)
    return result

print(combination(["a","b","c","d"], 2))
print(combination([1,2,3,4], 3))