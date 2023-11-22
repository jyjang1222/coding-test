num = int(input())
fac = 1

for i in range(1, num + 1):
   fac *= i
   
fac = str(fac)
cnt = 0

for i in range(len(fac)):
    idx = len(fac) - 1 - i
    if fac[idx] == '0':
        cnt += 1
    else:
        break
        
print(cnt)