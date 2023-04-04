
def solution(number, k):
    a = ""
    s = 0
    t = len(number) - k
    e = len(number) - t + 1
    i = 0
    while True:
        mx = -1
        mi = 0
        for i in range(s , e):
            if int(number[i]) == 9:
                mi =i
                mx =9
                break
            if int(number[i]) > int(mx):
                mi = i
                mx = number[i]
        a += str(number[mi])
        t -= 1
        if t == 0:
            break
        s = mi + 1
        e = len(number) - t + 1    
        pass      
    return a
number , k = "1924" , 2
number , k = "1231234" , 3
number , k = "4177252841" , 4
number , k = "1234567" , 3 # "4567"
number , k = "321924" , 2 # 3924
r = solution(number , k)
print(r)