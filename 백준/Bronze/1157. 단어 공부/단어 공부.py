str = input().upper()

chrs = list(set(str))

max = 0
maxCh = ''
for ch in chrs:
    count = str.count(ch)
    if count > max:
        max = count
        maxCh = ch
    elif str.count(ch) == max:
        maxCh = '?'

print(maxCh)