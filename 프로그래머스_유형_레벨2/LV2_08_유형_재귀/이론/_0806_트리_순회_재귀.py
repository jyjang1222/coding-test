

class Node:
    key = None
    data = None
    left = None
    right = None

class Tree:
    root = None
    def addKey(self , key , data):
        node = Node()
        node.key = key
        node.data = data

        if self.root is None:
            self.root = node
            print("root : " , key)
            return
        
        cur = self.root
        while True:
            if cur.key == key:
                print("중복키 : " , key)
                break
            elif cur.key > key:
                if cur.left is None:
                    cur.left = node
                    print("left : " , key)
                    break
                cur = cur.left
            elif cur.key < key:
                if cur.right is None:
                    cur.right = node
                    print("right : " , key)
                    break
                cur = cur.right
        pass

    def preOrderPrint(self):
        print("--- preOrder ---")
        self.preOrderTree(self.root)
        print("--- preOrder ---")

    def preOrderTree(self, cur):
        if cur != None:
            print(cur.key)
            if cur.left != None:
                self.preOrderTree(cur.left)
            if cur.right != None:
                self.preOrderTree(cur.right)
        
    def inOrderPrint(self):
        print("--- inOrder ---")
        self.inOrderTree(self.root)
        print("--- inOrder ---")

    def inOrderTree(self, cur):
        if cur != None:        
            if cur.left != None:
                self.inOrderTree(cur.left)
            print(cur.key)
            if cur.right != None:
                self.inOrderTree(cur.right)

    def postOrderPrint(self):
        print("--- postOrder ---")
        self.postOrderTree(self.root)
        print("--- postOrder ---")

    def postOrderTree(self, cur):
        if cur != None:        
            if cur.left != None:
                self.postOrderTree(cur.left)      
            if cur.right != None:
                self.postOrderTree(cur.right)
            print(cur.key)

    def levelOrderPrintQueue(self):
        q = []
        q.append(self.root)
        print("--- levelOrder ---")
        while True:
            if len(q) == 0:
                break
            front = q.pop(0)
            print(front.key)
            if front.left:
                q.append(front.left)
            if front.right:
                q.append(front.right)
        print("--- levelOrder ---")

    def heightPrint(self):
        h = self.getHeightTree(self.root)
        print("height : " , h)

    def getHeightTree(self , cur):
        if cur is None:
            return 0
        mx = max(self.getHeightTree(cur.left) , self.getHeightTree(cur.right)) + 1
        return mx
    
    def sizePrint(self):
        s = self.getSizeTree(self.root)
        print('size : ' , s)

    def getSizeTree(self, cur):
        if cur is None:
            return 0
        count = 1 + self.getSizeTree(cur.left) + self.getSizeTree(cur.right)
        return count
    
tree = Tree()
tree.addKey(10, "a")
tree.addKey(8, "a")
tree.addKey(9, "a")
tree.addKey(7, "a")
tree.addKey(12, "a")
tree.addKey(14, "a")
tree.addKey(16, "a")
tree.addKey(15, "a")
tree.preOrderPrint()
tree.inOrderPrint()
tree.postOrderPrint()
tree.levelOrderPrintQueue()
tree.heightPrint()
tree.sizePrint()
