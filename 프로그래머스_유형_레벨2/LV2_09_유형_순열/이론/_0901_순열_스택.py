# https://bcp0109.tistory.com/14

class Node:
    depth = 0
    arr = []

def swap(arr , i , depth):
    arr[i] , arr[depth] = arr[depth] , arr[i]

def printPerm(arr , n):
    for i in range(n):
        print(arr[i] , end=" ")
    print()

def permutationStack(arr, n):
    result = []
    stack = []
    node = Node()
    node.arr = arr.copy()
    stack.append(node)

    while True:
        if len(stack) == 0:
            break
        pop = stack.pop()
        if pop.depth == n:
            printPerm(pop.arr , n)
            continue

        for i in range(pop.depth , len(pop.arr)):
            temp = Node()
            temp.arr = pop.arr.copy()
            temp.depth = pop.depth + 1
            swap(temp.arr , i , pop.depth)
            stack.append(temp)
        
    return result
    
print(permutationStack([1,2,3], 3))
print("-----")
print(permutationStack([1,2,3], 2))