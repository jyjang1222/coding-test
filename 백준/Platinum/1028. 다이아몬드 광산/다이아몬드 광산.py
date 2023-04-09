import sys
row, col = map(int, sys.stdin.readline().split())
rowcol = [row, col]
map = ''
for i in range(row):
    map += sys.stdin.readline().rstrip()

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
            idx1 = size - 1 + j*col + k
            idx2 = idx1
            idx3 = idx1+(col*(2*(size)-2))
            idx4 = idx3
            if chk:
                for m in range(size):
                    if map[idx1] == '0' or map[idx2] == '0' or map[idx3] == '0' or map[idx4] == '0':
                        chk = False
                        break
                    idx1 += num1
                    idx2 += num2
                    idx3 -= num1
                    idx4 -= num2
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