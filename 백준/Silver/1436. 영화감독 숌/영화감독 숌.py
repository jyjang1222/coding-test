N = int(input())
count = 0
num = 665
sample = '666'

while count < N:
    num += 1
    nan = str(num)
    for i in range(len(nan) - len(sample) + 1):
        if nan[i] == '6' and nan[i+1] == '6' and nan[i+2] == '6':
            count += 1
            break

print(num)