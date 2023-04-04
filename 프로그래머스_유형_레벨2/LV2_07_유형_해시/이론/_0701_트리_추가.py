# 트리 : 중복된키를 허용하지않는 자료구조 
# 트리 전체 설명 : https://starrykss.tistory.com/1911

# 삽입 : https://deok2kim.tistory.com/104

class Node:
    key = None
    data = None
    left = None
    right = None

class Tree:
    root = None
    def addNode(self , key , data):
        node = Node()
        node.key = key
        node.data = data

        if self.root == None:
            self.root = node
            print("root : " , key)
            return
        
        curNode = self.root

        while True:
            if key == curNode.key:
                print("중첩키 : " , key)
                break

            elif key < curNode.key:
                if curNode.left == None:
                    curNode.left = node
                    print("left : " , key)
                    break 
                curNode = curNode.left
                pass

            elif key > curNode.key:
                if curNode.right == None:
                    curNode.right = node
                    print("right : " , key)
                    break
                curNode = curNode.right
                pass

    def printTreeStack(self):
        print("-------------------------")
        if self.root == None:
            print("print : None")
            return
        stack = []
        curNode = self.root

        while True:
            while True:
                if curNode == None:
                    break
                stack.append(curNode)
                curNode = curNode.left
            if len(stack) == 0:
                break
            curNode = stack.pop()
            print(curNode.key)       
            curNode = curNode.right
        print("-------------------------")
        pass


    


tree = Tree()
tree.printTreeStack()
tree.addNode(10 , 100)
tree.addNode(9 , 100)
tree.addNode(15, 100)
tree.addNode(11, 100)
tree.addNode(12, 100)
tree.addNode(14 , 100)
tree.addNode(13 , 100)
tree.addNode(16 , 100)
tree.addNode(10 , 100)
tree.printTreeStack()


