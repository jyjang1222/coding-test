"""
    
아래 리스트에서 각 알파벳 별 개수를 출력하시오.
[정답]
    {'a': 3, 'b': 1, 'c': 1, 'd': 4, 'e': 2, 's': 3, 'w': 3, 'f': 1}

"""
a = "abcdesdweasfsdwadw"
mydi = {}

for i in range(len(a)):
    if a[i] in mydi:
        mydi[a[i]] += 1
    else:
        mydi[a[i]] = 1

print(mydi)
