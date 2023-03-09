chess1 = [
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW'
]
chess2 = [
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB'
]

row, col = map(int, input().split())
map = []

for _ in range(row):
    map.append(input())

min1 = 999
min2 = 999

for i in range(len(map) - 7):
    for j in range(len(map[i]) - 7):
        count1 = 0
        count2 = 0
        for k in range(8):
            for m in range(8):
                if map[k+i][m+j] != chess1[k][m]:
                    count1 += 1
                if map[k+i][m+j] != chess2[k][m]:
                    count2 += 1
        if count1 < min1:
            min1 = count1
        if count2 < min2:
            min2 = count2

if min1 > min2:
    print(min2)
else:
    print(min1)