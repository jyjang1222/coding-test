test = int(input())

ans = 'O'
for i in range(test):
    score = 0
    string = input()
    add = 1
    for c in string:
        if c == ans:
            score += add
            add += 1
        else:
            add = 1
    print(score)