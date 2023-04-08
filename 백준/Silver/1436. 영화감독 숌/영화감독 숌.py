N = int(input())
count = 0
num = 665
sample = '666'

while count < N:
    num += 1
    nan = str(num)
    
    if sample in nan:
        count += 1

print(num)