import sys
row, col = map(int, sys.stdin.readline().split())
rowcol = [row, col]
map = ''
for i in range(row):
    map += sys.stdin.readline().rstrip()
# print(map)
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
                    print(idx1,idx2,idx3,idx4,m)
                    if map[idx1] == '0' or map[idx2] == '0' or map[idx3] == '0' or map[idx4] == '0':
                        chk = False
                        break
                    idx1 += num1
                    idx2 += num2
                    idx3 -= num1
                    idx4 -= num2
                # for m in range(size):
                #     # print(idx1,idx2,m)
                #     if map[idx1] == '0' or map[idx2] == '0':
                #         chk = False
                #         break
                #     idx1 += num2
                #     idx2 += num1
                # 7 7
                # 0001000
                # 0010100
                # 0100010
                # 1000001
                # 0100010
                # 0010101
                # 0000010
                # 4
                # for m in range(size - 1):
                #     if map[idx] == '0':
                #         chk = False
                #         break
                #     idx -= num1
                # for m in range(size - 1):
                #     if map[idx] == '0':
                #         chk = False
                #         break
                #     idx -= num2
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

# 1 1x1
# 2 3x3
# 3 5x5
# 4 7x7

# size 1
# 0

# size 2
# 3*3   4 2
#  1 
# 3 5 
#  7
# 3*4    5 3
# 0020
# 0507
# 00100
# 4x4     5 3
# 0000
# 0100  5
# 1010 8 10
# 0100  13   row

# size 3  6 4
#    2 
#   6 8 
# 10   14
#  16 18 
#    22

# size 4  8 6
# 0 0 0 3 0 0 0
# 0 0 9 0 11 0 0
# 0 15 0 0 0 19 0
# 21 0 0 0 0 0 27
# 0 29 0 0 0 33 0
# 0 0 37 0 39 0 0
# 0 0 0 45 0 0 0