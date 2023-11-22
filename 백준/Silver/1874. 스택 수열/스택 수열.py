def pushStack(num):
    stack.append(num)
    
def popStack():
    stack.pop()

stackLog = ''
N = int(input())
Answer = []
stack = []

for i in range(N):
    Answer.append(int(input()))

idx = 0
for i in range(1, N+1):
    pushStack(i)
    stackLog += '+'
    while len(stack) > 0 and stack[len(stack)-1] == Answer[idx]:
        idx += 1
        popStack()
        stackLog += '-'

if len(stack) > 0:
    print('NO')
else:
    for i in stackLog:
        print(i)