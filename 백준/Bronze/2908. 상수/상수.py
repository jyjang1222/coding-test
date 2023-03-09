A, B = input().split()

arr1, arr2 = list(A), list(B)

n1 = ''
n2 = ''

for i in range(len(arr1)):
    lastIdx = len(arr1) - 1
    n1 += arr1[lastIdx - i]
    n2 += arr2[lastIdx - i]

max = int(n1)

if int(n2) > max:
    max = n2

print(max)