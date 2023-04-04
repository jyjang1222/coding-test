# https://school.programmers.co.kr/learn/courses/30/lessons/12905

# https://dev-note-97.tistory.com/107

def solution(board):
    mx = 0
    for i in range(1 , len(board)):
        for j in range(1, len(board[i])):
            if board[i][j] != 0:
                a = board[i-1][j-1]
                b = board[i-1][j]
                c = board[i][j-1]
                mi = min(a,b,c)
                board[i][j] = mi + 1
                if mx < board[i][j]:
                    mx = board[i][j]
    if mx == 0 and max(board[0]) > 0:
        return 1    
    return mx * mx

b = [[0, 1, 1, 0],[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0]]
r = solution(b)
print(r)