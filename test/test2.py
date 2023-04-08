row, col = map(int, input().split())
rowcol = [row, col]
map = ''
for i in range(row):
    map += input()

maxSize = min(rowcol) + 1
maxSize //= 2

size = maxSize

while size > 1:
    num1 = (size * 2) + (col - (2 * size - 1))
    num2 = num1 - 2

    loop1 = row - (2*size - 1)+1
    loop2 = col - (2*size - 1)+1 

    for j in range(loop1):
        for k in range(loop2):
            chk = True
            idx = size - 1 + j*col + k
            if chk:
                for m in range(size - 1):
                    if map[idx] == '0':
                        chk = False
                        break
                    idx += num1
                for m in range(size - 1):
                    if map[idx] == '0':
                        chk = False
                        break
                    idx += num2
                for m in range(size - 1):
                    if map[idx] == '0':
                        chk = False
                        break
                    idx -= num1
                for m in range(size - 1):
                    if map[idx] == '0':
                        chk = False
                        break
                    idx -= num2
            if chk:
                break
        if chk:
            break
    if chk:
        break
    size -= 1
if size == 1:
    if '1' not in map:
        size = 0

print(size)