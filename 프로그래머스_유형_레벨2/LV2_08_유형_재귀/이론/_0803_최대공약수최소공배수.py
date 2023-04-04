# 반복문
def gcd_loop(a , b):
    while True:
        if a % b == 0:
            return b
        else:
            c = a
            d = b
            a = d
            b = c % d

print(gcd_loop(4, 2))

# 재귀
def gcd(a , b):
    if a % b == 0:
        return b
    else:
        return gcd(b , a%b)  
     
print(gcd(4, 2))


#[최소공배수]
a = 24
b = 76

c = a * b // gcd(a , b)
print(c)







