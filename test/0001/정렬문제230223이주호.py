'''
[최종문제] 위 규칙을 가지고 아래 배열을 정렬하시오.

    [
        [6,5,4,5,5,8],
        [6,5,6],
        [6,5,4,5,5],
        [3,4,5,8,9,3,3,3]
        [9],
        [1,4,7]
    ]

    [
        [1,4,7]
        [3,4,5,8,9,3,3,3]
        [6,5,4,5,5],
        [6,5,4,5,5,8],
        [6,5,6],
        [9],
    ]
    정렬후
    [
        [1,4,7]
        [3,4,5,8,9,3,3,3]
        [6,5,4,5,5],
        [6,5,4,5,5,8],
        [6,5,6],
        [9],
    ]

'''

arr = [
    [6,5,4,5],
    [6,1],
    [6],
    [6,5],
    [6,5,4,5,5,8],
    [6,5,6],
    [6,2,1],
    [6,5,4,5,5],
    [6,1,6,8,5],
    [6,4,6,4],
    [6,5,4],
    [6,6],
    [6,0,6],
    [6,0],
    [6,5,4,5,4,1]
]

# 배열 안의 숫자 중에서 가장 최솟값을 구한다
min = arr[0][0]
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] < min:
            min = arr[i][j]

# 그 구한 최솟값에서 1을 뺌으로써 min은 배열에서 가장 최솟값이 된다
min -= 1


# 배열들의 길이를 구한다
lengthList = []
for v in arr:
    lengthList.append(len(v))

# 배열들 중에서 가장 긴 배열의 길이를 구한다
maxLen = lengthList[0]
for i in range(len(lengthList)):
    if lengthList[i] > maxLen:
        maxLen = lengthList[i]

# 모든 배열에 최솟값을 넣어 가장 긴 배열 길이에 길이를 맞춘다
for i in range(len(arr)):
    while len(arr[i]) < maxLen:
        arr[i].append(min)

idx = 0
while idx < maxLen:

    for i in range(len(arr)):
        for j in range(len(arr)):
            if idx == 0:
                if i < j and arr[i][idx] > arr[j][idx]:
                    arr[i], arr[j] = arr[j], arr[i]

            elif i < j and arr[i][idx - 1] == arr[j][idx - 1]: # 그 전 값들이 같다면
                if i < j and arr[i][idx - 2] == arr[j][idx - 2]: # 그 전전 값들이 같다면
                    if i < j and arr[i][idx] > arr[j][idx]: # 값을 비교해 정렬하기 때문에 최솟값이 들어간 배열은 항상 상단으로 올라간다
                        arr[i], arr[j] = arr[j], arr[i]

    idx += 1

# 이제 값을 정렬했으니 배열에 넣었던 최솟값을 뺀다    
result = [[] for _ in range(len(arr))]
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] != min:
            result[i].append(arr[i][j])

for v in result:
    print(v)
print()