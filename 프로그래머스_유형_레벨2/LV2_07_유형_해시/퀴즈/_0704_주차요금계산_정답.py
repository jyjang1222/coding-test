# https://school.programmers.co.kr/learn/courses/30/lessons/92341

def changeTime(s):
    temp = s.split(":")
    hour = int(temp[0]) * 60
    min = int(temp[1])
    time = hour + min
    return time
def solution(fees, records):
    arr = []
    di = {}
    for v in records:
        temp = v.split(" ")
        if temp[2] == "IN":
            arr.append(temp)
            pass
        if temp[2] == "OUT":
            
            outcar = []
            index = 0
            for i in range(len(arr)):
                if temp[1] in arr[i]:
                    outcar = arr[i]
                    index = i
                    break
            intime = changeTime(outcar[0])
            outtime = changeTime(temp[0])
            if outcar[1] in di:
                di[outcar[1]] += outtime - intime
            else:
                di[outcar[1]] = outtime - intime
            arr.remove(arr[index])
    #print("남은차 : " , arr)
    #print(di)
    for i in range(len(arr)):
        outcar = arr[i]
        intime = changeTime(outcar[0])
        outtime = changeTime("23:59")
        if outcar[1] in di:
            di[outcar[1]] += outtime - intime
        else:
            di[outcar[1]] = outtime - intime

    #print(di)
    arr =[]
    di = dict(sorted(di.items()))
    for v in di.keys():
        total = 0
        #print(v , di[v])
        time = di[v]
        if fees[0] >= time:
            total += fees[1]
        else:
            total += fees[1]
            time -= fees[0]

            addtime = 0
            addtime = time // fees[2]
            if time % fees[2] != 0:
                addtime += 1
            total += addtime * fees[3]
        arr.append(total)

    return arr

fees = [180, 5000, 10, 600]
records = [
"05:34 5961 IN", "06:00 0000 IN", 
"06:34 0000 OUT", "07:59 5961 OUT", 
"07:59 0148 IN", "18:59 0000 IN",
"19:09 0148 OUT", "22:59 5961 IN",
"23:00 5961 OUT"]

r = solution(fees , records)
print(r)