# https://school.programmers.co.kr/learn/courses/30/lessons/49994

def moveCheck( ny , nx):
    if ny < -5 or nx < -5:
        return False
    if ny > 5 or nx > 5:
        return False
    return True

def solution(dirs):
    y = 0
    x = 0
    arr = set()
    for i in range(len(dirs)):
        a = dirs[i]
        if a == 'U':
            if moveCheck(y - 1 , x):
                st = [y , x , y - 1 , x]
                st = ''.join(str(s) for s in st)
                arr.add(st)
                st = [y - 1 , x , y , x]
                st = ''.join(str(s) for s in st)
                arr.add(st)
                y -= 1
        elif a == 'L':
            if moveCheck(y , x - 1):
                st = [y , x , y , x-1]
                st = ''.join(str(s) for s in st)
                arr.add(st)
                st = [y  , x - 1, y , x]
                st = ''.join(str(s) for s in st)
                arr.add(st)
                x -= 1
        elif a == 'R':
            if moveCheck(y , x + 1):
                st = [y , x , y , x + 1]
                st = ''.join(str(s) for s in st)
                arr.add(st)
                st = [y  , x + 1, y , x]
                st = ''.join(str(s) for s in st)
                arr.add(st)
                x += 1
        elif a == 'D':
            if moveCheck(y + 1 , x):
                st = [y + 1, x , y , x]
                st = ''.join(str(s) for s in st)
                arr.add(st)
                st = [y  , x, y + 1, x]
                st = ''.join(str(s) for s in st)
                arr.add(st)
                y += 1

    
    result = len(arr) // 2
    return result
dirs = "ULURRDLLU"
#dirs = "LULLLLLLU"
r = solution(dirs)
print(r)