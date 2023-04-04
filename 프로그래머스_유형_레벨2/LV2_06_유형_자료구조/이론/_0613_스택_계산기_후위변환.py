
# 계산기
# 수식 변경 ==> data 의 문자열을 한글자씩 아래 조건을 실행한다.
# 1) 숫자면 calc 에 저장
# 2) 연산자면 ( , ) , +- , */ 에따라 달라진다.
# 3) 1. stack 의 길이가 0 이면 그냥 stack 에 저장
# -------  stack 의  길이 가 1 보다 크면 아래 조건 실행 ----------
#    2. ( 이면 그냥 stack 에 저장
#    3. ) 이면 소괄호를 만날때까지 전부 꺼내서 calc 에 저장
#    4-1. +- 이면 stack 에 있는 마지막 값 이 ( 이면 그냥 stack 에저장
#    4-2. +- 이면 stack 에 있는 마지막 값 이 ( 가아니면 한개끄내서 calc 에 저장후 +- 를 stack 에 저장
#    5-1. */ 이면 stack 에 있는 마지막 값이 */ 이면 한개끄내서 calc 에 저장후 */를 stack 에 저장
#    5-2. */ 이면 stack 에 있는 마지막 값이 */ 이 아니면 그냥 stack 에 저장
#    6. 전부 끝난후 stack 에 남아있는 연산자를 모두 꺼내서 calc 에 저장
# -----------------------------------------------------------


def changeData(data):

    calc = []
    stack = []

    for i in data:
        num = "0123456789"
        if i in num:
            calc.append(i)
        elif len(stack) == 0:
            stack.append(i)
        elif i == "(":
            stack.append(i)
        elif i == ")":
            while True:
                top = stack.pop()
                if top != "(":
                    calc.append(top)
                else:
                    break
        elif i == "+" or i == "-":
            if stack[-1] == "(":
                stack.append(i)
            else:
                top = stack.pop()
                calc.append(top)
                stack.append(i)
        elif i == "*" or i == "/":
            if stack[-1] == "*" or stack[-1] == "/":
                top = stack.pop()
                calc.append(top)
                stack.append(i)
            else:
                stack.append(i)
    while True:
        if len(stack) == 0:
            break
        else:
            top = stack.pop()
            calc.append(top)
    return calc


data = "1+3*(5+3*2)/2"
# data = "1+3*5+3"
data = changeData(data)
print(data)
