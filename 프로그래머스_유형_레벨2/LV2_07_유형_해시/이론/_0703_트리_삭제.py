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


    def deleteNode(self , key):
        if self.root == None:
            print("delet : None")
            return
        
        curNode = self.root
        parNode = None
        while True:
            if curNode.key == key:
                break
            elif curNode.key > key:
                if curNode.left == None:
                    print("delete not find : " , key)
                    return
                parNode = curNode
                curNode = curNode.left
                pass

            elif curNode.key < key:
                if curNode.right == None:
                    print("delete not find : " , key)
                    return
                parNode = curNode
                curNode = curNode.right
                pass

        print("delete find : " , key)
        if curNode.left == None and curNode.right == None:
            print("children : 0 ")
            if curNode == self.root:
                self.root = None
                return
            if parNode.left == curNode:
                parNode.left = None
            elif parNode.right == curNode:
                parNode.right = None

        elif curNode.left == None or curNode.right == None:
            print("children : 1")
            if curNode == self.root:
                if curNode.left == None:
                    curNode = curNode.right

                elif curNode.right == None:
                    curNode = curNode.left
            
            else:
                if parNode.left == curNode:
                    if curNode.left == None:
                        parNode.left = curNode.right

                    elif curNode.right == None:
                        parNode.left = curNode.left
                elif parNode.right == curNode:
                    if curNode.left == None:
                        parNode.right = curNode.right
                    elif curNode.right == None:
                        parNode.right = curNode.left
        else:
            print("children : 2")
            changePar = curNode
            changeChild = curNode.left
            while True:
                if changeChild.right != None:
                    changePar = changeChild
                    changeChild = changeChild.right
                else:
                    break
            print(changePar.key , changeChild.key)
            if changePar.left == changeChild:
                changePar.left = None
            elif changePar.right == changeChild:
                changePar.right = None
            curNode = changeChild


tree = Tree()
tree.printTreeStack()
tree.deleteNode(11)
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
tree.deleteNode(11)
#tree.deleteNode(16)
tree.printTreeStack()
tree.deleteNode(14)
tree.deleteNode(12)
tree.printTreeStack()

