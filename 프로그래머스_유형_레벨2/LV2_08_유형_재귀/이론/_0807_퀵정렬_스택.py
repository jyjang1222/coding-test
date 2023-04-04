
class Node:
    start = 0
    end = 0
def quick_sort_stack(arr):

    stack = []
    node = Node()
    node.pivot = 1
    node.end = len(arr) - 1
    node.start = 0
    stack.append(node)
    while True:
        if len(stack) == 0:
            break
        pop = stack.pop()
        if pop.start >= pop.end:
            continue

        start = pop.start
        end = pop.end
        pivot = start
        left = start + 1
        right = end
        while left <= right:
            while left <= end and arr[left] <= arr[pivot]:
                left += 1
            while right > start and arr[right] >= arr[pivot]:
                right -= 1
            if left > right:
                temp = arr[pivot]
                arr[pivot] = arr[right]
                arr[right] = temp
            else:
                temp = arr[left]
                arr[left] = arr[right]
                arr[right] = temp
        node = Node()
        node.start = start 
        node.end = right-1
        stack.append(node)
        node = Node()
        node.start = right + 1
        node.end = end
        stack.append(node)

arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
quick_sort_stack(arr)
print(arr)