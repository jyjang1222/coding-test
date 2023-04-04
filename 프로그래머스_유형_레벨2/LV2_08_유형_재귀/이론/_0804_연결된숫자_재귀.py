

def findNumber(dataMap , i , j , num):
    if i < 0 or j < 0 or i >= len(dataMap) or j >= len(dataMap):
        return

    if dataMap[i][j] == 1:
        dataMap[i][j] = num
    else:
        return 
    findNumber(dataMap , i + 1 , j , num)
    findNumber(dataMap , i - 1 , j , num)
    findNumber(dataMap , i , j - 1, num)
    findNumber(dataMap , i , j + 1, num)

def setColor(dataMap , num):
    for i in range(len(dataMap)):
        for j in range(len(dataMap[i])):
            if dataMap[i][j] == 1 : 
                findNumber(dataMap , i , j , num)
                num -= 1
                pass
            pass
    pass

dataMap = [
        [0,0,0,0,0,0,0,0,0,0],
        [0,1,1,1,1,0,1,1,1,1],
        [0,0,0,0,1,0,0,0,1,0],
        [0,0,0,0,1,0,0,0,1,0],
        [0,0,1,0,0,0,0,0,1,0],
        [0,1,1,1,0,0,1,0,0,0],
        [1,0,1,0,1,0,1,1,1,0],
        [0,1,1,1,0,0,1,0,1,1],
        [0,0,1,0,0,0,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0]]


num = 9
setColor(dataMap , num)
for i in range(len(dataMap)):
    print(dataMap[i])


