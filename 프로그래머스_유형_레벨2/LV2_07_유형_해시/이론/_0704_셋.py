"""
    
아래 리스트에서 중복되지않은 숫자만 모으시오.
"""
a = [3,6,5,8,8,6,5,1,2]
myset = set()

for i in range(len(a)):
    myset.add(a[i])

print(myset)
