# https://school.programmers.co.kr/learn/courses/30/lessons/42746

class Node:
    a = ""
    b = ""
    def print(self):
        print(self.b)
        
def printList(nodeList):
    for v in nodeList:
        v.print()
    print("----------------------")
def solution(numbers):
    if sum(numbers) == 0:
        return "0"
    nodeList =[]
    for i in range(len(numbers)):
        node = Node()
        node.a = str(numbers[i])
        node.b = str(numbers[i]) * 3
        nodeList.append(node)
    #printList(nodeList)
    
    nodeList = sorted(nodeList, key=lambda x: x.b , reverse=True)
    answer = ""
    for i in range(len(nodeList)):
        answer += nodeList[i].a
    
    return answer
   

print(solution([6, 10, 2]))             # result : 6210
#print(solution([3, 30, 34, 5, 9]))      # result : 9534330
print(solution([0,0,0,0]))  