

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
            print("root : " , key )
            return
        
        cur = self.root
        while True:
            if cur.key == key:
                print("중복키 : " , key)
                return
            
            elif cur.key < key:
                if cur.right is None:
                    print("right : " , key)
                    cur.right = node
                    return
                else:
                    cur = cur.right
                pass

            elif cur.key > key:
                if cur.left is None:
                    print("left : " , key)
                    cur.left = node
                    return
                else:
                    cur = cur.left             
        pass
    
    def preOrderPrintStack(self):
        print("----preOrderPrint----")
        if self.root is None:
            print("None")
            return  
        cur = self.root
        stack = []
        while True:
            while True:
                if cur == None:
                    break
                print(cur.key)
                stack.append(cur)
                cur = cur.left
            if len(stack) == 0:
                break
            cur = stack.pop()
            cur = cur.right
        pass

    def inOrderPrintStack(self):
        print("----inOrderPrint----")
        if self.root is None:
            print("None")
            return
        cur = self.root
        stack = []
        while True:
            while True:
                if cur is not None:
                    stack.append(cur)
                    cur = cur.left
                else:
                    break
            if len(stack) == 0:
                break
            cur = stack.pop()
            print(cur.key)
            cur = cur.right
        pass
    
    def postOrderPrintStack(self):
        print("----postOrderPrint----")
        stack = []
        cur = self.root
        check= []
        while True:      
            while True:
                if cur == None or cur.key in check:
                    break
                elif cur.key not in check:
                    if cur not in stack:
                        stack.append(cur)
                    cur = cur.left
            if len(stack) == 0:
                break    
            cur = stack[-1]
            if cur.right != None and cur.right.key not in check:    
                stack.append(cur.right)
                cur = cur.right
            elif cur.key : 
                print(cur.key)
                check.append(cur.key)
                stack.pop()
    
    def levelOrderPrintQueue(self):
        print("----levelOrder----")
        stack = []
        stack.append(self.root)
        while True:
            if len(stack) == 0:
                break
            cur = stack.pop(0)
            print(cur.key)
            if cur.left != None:
                stack.append(cur.left)
            if cur.right != None:
                stack.append(cur.right)
        pass
    def sizePrintStack(self):
        print("----sizePrintStack----")
        size = 0
        stack = []
        stack.append(self.root)
        size += 1
        while True:
            if len(stack) == 0:
                break
            cur = stack.pop(0)
            #print(cur.key)
            if cur.left != None:
                stack.append(cur.left)
                size += 1
            if cur.right != None:
                stack.append(cur.right)
                size += 1
        print("size : " , size)

    def heightPrintStack(self):
        print("----heightPrintStack----")
        stack = []
        stack.append(self.root)
        height = [1]
        mx = 0
        while True:
            if len(stack) == 0:
                break
            cur = stack.pop(0)
            h = height.pop(0)
            if h > mx:
                mx = h
            if cur.left != None:
                height.append(h + 1)
                stack.append(cur.left)
            if cur.right != None:
                height.append(h + 1)
                stack.append(cur.right)
        print("height : " , mx)
        pass

tree = Tree()
tree.addKey(20, "a")
tree.addKey(8, "a")
tree.addKey(14, "a")
tree.addKey(13, "a")
tree.addKey(5, "a")
tree.addKey(1, "a")
tree.addKey(12, "a")
tree.addKey(16, "a")
tree.addKey(17, "a")
tree.addKey(26, "a")
tree.addKey(30, "a")
tree.addKey(29, "a")
tree.preOrderPrintStack()
tree.inOrderPrintStack()
tree.postOrderPrintStack()
tree.levelOrderPrintQueue()
tree.sizePrintStack()
tree.heightPrintStack()