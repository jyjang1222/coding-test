import random
class MyHash:
    size = 0
    keyList = []
    dataList = []

    def setSize(self , size):
        self.size = size
        self.keyList = [None for i in range(size)]
        self.dataList = [None for i in range(size)]

    def getHash(self , key):
        return key % self.size

    def put(self , key , data):
        index = self.getHash(key)
        for i in range(self.size):
            if self.keyList[index] is None:
                self.keyList[index] = key
                self.dataList[index] = data
                print(index , key )
                break
            if self.keyList[index] == key:
                print("중복키" , index, key)
                break
            index += i
            index %= self.size
            if i == self.size - 1:
                print("저장할곳이 없습니다." , key)

    def get(self , key):
        index = self.getHash(key)
        for i in range(self.size):
            if self.keyList[index] == key:
                print("find : " , index , key)
                break

            index += i
            index %= self.size
            if i == self.size - 1:
                print("찾는 값이 없습니다. " , key)

    def printHash(self):

        for i in range(self.size):
            print(self.keyList[i] , self.dataList[i])



sample = "abcdefghijklmn"
size = 10
h = MyHash()
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



