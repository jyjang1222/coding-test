myset = set()
N = int(input())

for i in range(N):
    myset.add(input())

myset = list(myset)
myset.sort()
myset.sort(key = lambda x: len(x))

for v in myset:
    print(v)