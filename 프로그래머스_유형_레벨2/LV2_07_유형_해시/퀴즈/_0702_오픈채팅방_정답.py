# https://school.programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    answer = []
    di = {}
    for i in range(len(record)):
        token = record[i].split(" ")
        msg = token[0]
        id = token[1]
        if msg == "Enter":
            di[id] = token[2]
        elif msg == "Change":
            di[id] = token[2]
    for i in range(len(record)):
        token = record[i].split(" ")
        msg = token[0]
        id = token[1]
        if msg == "Enter":
            st = di[id] + "님이 들어왔습니다."
            answer.append(st)
        elif msg == "Leave":
            st = di[id] + "님이 나갔습니다."
            answer.append(st)
                
    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
r = solution(record)
print(r)