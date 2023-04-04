# 파이썬 스택
# https://daimhada.tistory.com/105

class Node:  # Node 클래스
    def __init__(self, item, link): # Node 생성자     
        self.item = item           
        self.next = link

def push(item):  # push 연산
    global top
    global size
    top = Node(item, top)  
    size += 1

def peek():  # peek 연산
    if size != 0:
        return top.item 

def pop():  # pop 연산
    global top
    global size
    if size != 0:
        top_item = top.item
        top = top.next
        size -= 1
        return top_item

def print_stack():  # 스택 출력
    print('전체출력 -> ', end='')
    p = top
    while p:
        if p.next is not None:
            print(p.item, '-> ', end='')
        else:
            print(p.item, end='')
        p = p.next
    print()

top = None
size = 0
push('apple')
push('orange')       
push('cherry')       
print_stack()
print('top 항목: ', end='')
print(peek())              
push('pear') 
print_stack()
pop()               
push('grape')
print_stack()