# 링크드 리스트 
class Node:
    data = None
    next = None

class Head:
    head = None
    size = 0

def insertData(head , data):
    temp = Node()
    temp.data = data
    pre = head
    for i in range(head.size):
        pre = pre.next
    
    pre.next = temp
    head.size += 1

def printLinkedList(head):
    print("------------------------")
    pre = head
    for i in range (pre.size):
        pre = pre.next
        print(i + 1 , " : " , pre.data)
    print("------------------------")
    
def deleteData(head , index):
    pre = head
    for i in range(int(index)):
        pre = pre.next
    if index == head.size:
        pre.next = None
    else:
        temp = pre.next
        pre.next = temp.next
    head.size -= 1


def searchData(head , index):
    pass

def play(head):
    while True:
        printLinkedList(head)
        print("[1] 삽입 [2]삭제 [3]검색[0]종료")
        sel = input()
        if sel == "1":
            print("추가할데이터입력 : ")
            data = input()
            insertData(head , data)
        elif sel == "2":
            print("삭제할인덱스입력 : ")
            index = input()
            deleteData(head , index)
        elif sel == "3":
            print("[과제]")
            pass

        elif sel == "0":
            break

head = Head()
play(head)



