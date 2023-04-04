# https://school.programmers.co.kr/learn/courses/30/lessons/76502

def solution(s):
    answer = []
    for i in range(len(s)):
        stack = []
        for j in range(len(s[i])):
            a = s[i][j]
            if len(stack) == 0:
                stack.append(a)
            else:
                if a == '(':
                    stack.append(a)
                elif a == ')':
                    peek = stack[-1]
                    if peek == '(' :
                        stack.pop()
                    else:
                        stack.append(a)
                        break
        if len(stack) > 0 :
            answer.append("no")
        else:
            answer.append("ok")
    
    return answer
s = ["((()))" ,"())(" , "()())(" , "(())()"]

r = solution(s)
print(r)

"""
괄호 모양이 전부 짝이 잘맞는지 확인 하시오.
괄호는 여는 괄호 ( 와 닫는 괄호 ) 로 이루어저있다.
배열의 모든 문자열을 검사하여 잘맞는 괄호는 'ok' 를 
잘안맞는 괄호는 'no' 를 저장하는 배열을 반환하시오.

[예시]
 [1] ((())) ok
 [2] ())(   no
 [3] ()())( no
 [4] (())() ok
"""