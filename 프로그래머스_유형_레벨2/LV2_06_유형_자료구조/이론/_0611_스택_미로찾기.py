# 스택의 활용
# 1) 미로찾기
dataMap = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,3,1,1,1,1,1,1,1,0],
    [0,0,0,0,0,1,0,1,0,0],
    [0,0,0,0,0,1,0,0,0,0],
    [0,1,1,1,1,1,1,0,0,0],
    [0,0,1,0,0,0,1,1,1,0],
    [0,0,1,0,0,0,0,1,0,0],
    [0,1,1,1,1,1,0,1,0,0],
    [0,0,0,0,0,0,0,2,0,0],
    [0,0,0,0,0,0,0,0,0,0]
 ]
mark = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
 ]
# 0 = "가로막힌 벽"
# 1 = "갈수있는 길"
# 2 = "도착"
# 3 = "시작"
# dir ==> 0:북 , 1:동 , 2:서 , 3:남
# mark ==> 이미지나간길 체크용
stack = []
data = {"x": 1, "y": 1, "dir": 0}
mark[data["y"]][data["x"]] = True
stack.append(data)
run = True
while run:
    if len(stack) == 0:
        print("못찾음")
        break
    top = stack.pop()
    print("top : " , top["x"], " ", top["y"] , " " ,top["dir"])
    while True:
        nextx = top["x"]
        nexty = top["y"]
        if top["dir"] == 4:
            break
        if top["dir"] == 0:
            nexty -= 1
        if top["dir"] == 1:
            nextx += 1
        if top["dir"] == 2:
            nexty += 1
        if top["dir"] == 3:
            nextx -= 1
        if nextx < 0 or nextx >= 10 \
            or nexty < 0 or nexty >= 10 \
            or mark[nexty][nextx] == 1 \
            or dataMap[nexty][nextx] == 0:
            print("못감 : " , top["dir"])
            top["dir"] += 1
            continue
        if dataMap[nexty][nextx] == 2:
            print("도착")
            run = False
            break
        if dataMap[nexty][nextx] == 1:
            mark[nexty][nextx] = 1
            top["dir"] += 1
            print("깇찾음 : " , top["x"], " ", top["y"], " ", top["dir"])
            stack.append(top)
            data = {"x": nextx, "y": nexty, "dir": 0}
            stack.append(data)
            break