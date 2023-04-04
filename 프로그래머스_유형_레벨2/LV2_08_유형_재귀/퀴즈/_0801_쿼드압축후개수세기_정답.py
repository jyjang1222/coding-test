# https://school.programmers.co.kr/learn/courses/30/lessons/68936

def quad(arr, x, y, l):
    for i in range(x, x + l):
        for j in range(y, y + l):
            if arr[i][j] != arr[x][y]:
                l = l // 2
                quad(arr, x, y, l)
                quad(arr, x, y + l, l)
                quad(arr, x + l, y, l)
                quad(arr, x + l, y + l, l)
                return

    answer[arr[x][y]] += 1

def solution(arr):
    global answer
    answer = [0, 0]

    quad(arr, 0, 0, len(arr))

    return answer


arr = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]
r = solution(arr)
print(r)