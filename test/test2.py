N = int(input())

mapcost = []
for i in range(N):
    arr = list(map(int, input().split()))
    mapcost.append(arr)
mapstate = input()
P = int(input())

dictstate = {}
for i in range(len(mapstate)):
    dictstate[i] = mapstate[i]

# print(mapcost)
# print(mapstate)
print(dictstate)

# for i in range(len(mapstate)):
#     mincost = 36
#     state = mapstate[i]