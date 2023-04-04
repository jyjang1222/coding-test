def push(stack, data):
    stack.append(data)

def pop(stack):
    if len(stack) == 0:
        print("비어있습니다")
        return
    else:
        return stack.pop()

stack = []
push(stack, 10)
push(stack, 20)
push(stack, 30)
print(stack)
print(pop(stack))
print(pop(stack))
print(pop(stack))
print(pop(stack))
print(stack)
