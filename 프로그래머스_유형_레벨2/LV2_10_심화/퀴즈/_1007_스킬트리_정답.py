# https://school.programmers.co.kr/learn/courses/30/lessons/49993

def solution(s, st):
    answer = 0
    
    for i in range(len(st)):
        for j in range(len(st[i])):
            if st[i][j] not in s:
                st[i] = st[i].replace(st[i][j] , " ")

        st[i] = st[i].replace(" " , "")
            
    #print(st)
    for i in range(len(st)):
        check= False
        for j in range(len(st[i])):
            print(st[j] , " " , s[j])
            if st[i][j] != s[j]:
                check = True
                break
        if check == False:
            answer += 1
    return answer


skill = "CBD"

skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]

r = solution(skill , skill_trees)
print(r)