# 스택 연결된 숫자 찾기 

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

num = 1
for i in range(len(dataMap)):
    for j in range(len(dataMap[i])):
        if dataMap[i][j] == 1:
            stack = []
            num += 1
            data = {"x": j, "y": i}
            stack.append(data)
            while True:
                if len(stack) == 0:
                    break
                top = stack.pop()
                y = top["y"]
                x = top["x"]
                dataMap[y][x] = num
                for ii in range(-1, 2):
                    c = False
                    for jj in range(-1, 2):
                        nextx = jj + x
                        nexty = ii + y
                        if nextx < 0 or nextx >= 10 or nexty < 0 or nexty >= 10 or (ii == 0 and jj == 0):
                            continue
                        if dataMap[nexty][nextx] == 1:
                            data = {"x": nextx, "y": nexty}
                            dataMap[nexty][nextx] = num
                            stack.append(data)
for i in dataMap:
    print(i)