starCount = int(input())

star = '*'
space = ' '
j = starCount - 1
for i in range(starCount):
    combine = space * j + star
    print(combine)
    star += '*'
    j -= 1