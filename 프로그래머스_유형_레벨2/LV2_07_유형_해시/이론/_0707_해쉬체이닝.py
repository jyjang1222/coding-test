
import random

class Node:
    key = None
    data = None
    next = None


class MyHashChaining:
    size = 0
    arr = []

    def setSize(self , size):
        self.size = size
        self.arr = [None for i in range(size)]


    def getHash(self , key):
        return key % self.size
    
    def put(self , key , data):
        index = self.getHash(key)

        pre = self.arr[index]
        if pre is not None:
            while True:
                if pre.key == key:
                    print("중복키" , key)
                    return
                if pre.next is None:
                    break
                pre = pre.next

        node = Node()
        node.key = key
        node.data = data
        node.next = pre
        self.arr[index] = node

    def printHash(self):
        for i in range(self.size):
            pre = self.arr[i]
            while True:
                if pre == None:
                    break
                print(pre.key , pre.data , end=" , ")
                pre = pre.next
            print()
    def get(self , key):
        index = self.getHash(key)
        pre = self.arr[index]
        while True:
            if pre == None:
                break
            if pre.key == key:
                print(key , pre.data)
                return
            pre = pre.next

h = MyHashChaining()
sample = "abcdefghijklmn"
size = 10
h.setSize(size)
for i in range(20):
    r = random.randint(0, 20)
    h.put(r , sample[r % size])
print("---------------------------")
h.printHash()
print("---------------------------")
for i in range(20):
    r = random.randint(0, 20)
    h.get(r)




            