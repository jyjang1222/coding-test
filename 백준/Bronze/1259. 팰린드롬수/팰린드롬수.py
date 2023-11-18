while True:
    res = 'yes'
    strNum = input()
    if strNum != '0':
        strLen = len(strNum)
        loopCnt = strLen // 2
        endIdx = strLen - 1
        for i in range(0, loopCnt):
            if strNum[i] != strNum[endIdx - i]:
                res = 'no'
        print(res)
    else:
        break