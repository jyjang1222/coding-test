arr = []
for i in range(10):
    arr.append(int(input()) % 42)

arr2 = list(set(arr))

print(len(arr2))