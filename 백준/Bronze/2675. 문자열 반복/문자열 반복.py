test = int(input())

for i in range(test):
    arr = input().split()
    count = int(arr[0])
    string = arr[1]
    res = ''
    for s in string:
        for j in range(count):
            res += s
    print(res)