"""
    [2차원배열정렬 ]

     조건 :  일차원배열 하나하나가 정렬기준이다.

    앞글자 하나의 기준으로 오름차순하면된다. 
    [
        [5,3]
        [2,9]
        [3,8]
    ]
    정렬후
    [
        [2,9]
        [3,8]
        [5,3]
    ]
    -------------------------------------
    앞글자가 같은경우
    [
        [5,3]
        [5,1]
        [2,8]
    ]
    정렬후
    [
        [2,8]
        [5,1]
        [5,3]
    ]
    -------------------------------------
    길이가 다른경우 (각글자를 비교후 짧은배열이 위로올라간다.)
    단, 앞글자가 작은숫자라면 길이상관없이 맨위로 간다. 
    [
        [5,7,2]
        [5,7]
        [1,5,6,45,6]
    ]
    정렬후
    [
        [1,5,6,45,6]
        [5,7]
        [5,7,2]
    ]
    -------------------------------------
    [최종문제] 위 규칙을 가지고 아래 배열을 정렬하시오.

    [
        [6,5,4,5,5,8],
        [6,5,6],
        [6,5,4,5,5],
        [3,4,5,8,9,3,3,3]
        [9],
        [1,4,7]
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
"""

arr1 = [
        [5,3],
        [2,9],
        [3,8]
    ]
arr2 = [
        [5,3],
        [5,1],
        [2,8]
    ]
arr3 = [
        [5,7,2],
        [5,7],
        [1,5,6,45,6]
    ]
arr4 = [
        [6,5,4,5,5,8],
        [6,5,6],
        [6,5,4,5,5],
        [3,4,5,8,9,3,3,3],
        [9],
        [1,4,7]
    ]
# 342150
arr5 = [
        [6,5],
        [6,5,6],
        [6,5,4,5,5,8],
        [0],
        [6,5,4,5,5],
        [3,4,5,8,9,3,3,3],
        [6,5,4],
        [9],
        [1,4,7]
    ]
# 376052481

# 1
gradeIdx = []

for i in range(len(arr1)):
    grade = 0
    first = arr1[i][0]
    for j in range(len(arr1)):
        if first > arr1[j][0]:
            grade += 1
    gradeIdx.append(grade)

print(gradeIdx)

ans1 = []

for i in range(len(arr1)):
    for j in range(len(gradeIdx)):
        if i == gradeIdx[j]:
            ans1.append(arr1[j])

print(ans1)

# 2
gradeIdx = []

for i in range(len(arr2)):
    grade = 0
    first = arr2[i][0]
    for j in range(len(arr2)):
        if first > arr2[j][0]:
            grade += 1
        elif first == arr2[j][0]:
            for k in range(len(arr2[i])):
                if arr2[i][k] > arr2[j][k]:
                    grade += 1
                    break

    gradeIdx.append(grade)

print(gradeIdx)

ans2 = []

for i in range(len(arr2)):
    for j in range(len(gradeIdx)):
        if i == gradeIdx[j]:
            ans2.append(arr2[j])

print(ans2)

# 3
gradeIdx = []

for i in range(len(arr3)):
    grade = 0
    first = arr3[i][0]
    for j in range(len(arr3)):
        if first > arr3[j][0]:
            grade += 1
        elif first == arr3[j][0]:
            chk = True
            for k in range(len(arr3[i])):
                if k >= len(arr3[j]):
                    continue
                if arr3[i][k] > arr3[j][k]:
                    chk = False
                    grade += 1
                    break
            if chk:
                if len(arr3[j]) < len(arr3[i]):
                    grade += 1


    gradeIdx.append(grade)

print(gradeIdx)

ans3 = []

for i in range(len(arr3)):
    for j in range(len(gradeIdx)):
        if i == gradeIdx[j]:
            ans3.append(arr3[j])

print(ans3)

# 4
gradeIdx = []

for i in range(len(arr4)):
    grade = 0
    first = arr4[i][0]
    for j in range(len(arr4)):
        if first > arr4[j][0]:
            grade += 1
        elif first == arr4[j][0]:
            chk = True
            for k in range(len(arr4[i])):
                if k >= len(arr4[j]):
                    continue
                if arr4[i][k] > arr4[j][k]:
                    chk = False
                    grade += 1
                    break
            if chk:
                if len(arr4[j]) < len(arr4[i]):
                    grade += 1


    gradeIdx.append(grade)

print(gradeIdx)

ans4 = []

for i in range(len(arr4)):
    for j in range(len(gradeIdx)):
        if i == gradeIdx[j]:
            ans4.append(arr4[j])

print(ans4)

# 4.2
gradeIdx = []

for i in range(len(arr4)):
    grade = 0
    first = arr4[i][0]
    for j in range(len(arr4)):
        if first > arr4[j][0]:
            grade += 1
        elif first == arr4[j][0]:
            chk = True
            for k in range(len(arr4[j])):
                if k >= len(arr4[i]) or k >= len(arr4[j]):
                    continue
                if arr4[i][k] > arr4[j][k]:
                    chk = False
                    grade += 1
                    break
            if chk:
                if len(arr4[j]) < len(arr4[i]):
                    grade += 1
    gradeIdx.append(grade)

print(gradeIdx)

ans4 = []

for i in range(len(arr4)):
    for j in range(len(gradeIdx)):
        if i == gradeIdx[j]:
            ans4.append(arr4[j])

print(ans4)

# 5
gradeIdx = []

for i in range(len(arr5)):
    grade = 0
    first = arr5[i][0]
    for j in range(len(arr5)):
        if first > arr5[j][0]:
            grade += 1
        elif first == arr5[j][0]:
            chk = True
            for k in range(len(arr5[i])):
                if k >= len(arr5[j]):
                    continue
                if arr5[i][k] > arr5[j][k]:
                    chk = False
                    grade += 1
                    break
            if chk:
                if len(arr5[j]) < len(arr5[i]):
                    grade += 1


    gradeIdx.append(grade)

print(gradeIdx)

ans5 = []

for i in range(len(arr5)):
    for j in range(len(gradeIdx)):
        if i == gradeIdx[j]:
            ans5.append(arr5[j])

print(ans5)