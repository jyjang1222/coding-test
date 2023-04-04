def insertNode(linkedList , data):
    node = {"data" : data, "next" : None}
    if linkedList["size"] == 0:
        linkedList["next"] = node
    else:
        pre = linkedList["next"]
        for i in range(linkedList["size"]-1):
                pre = pre["next"]
        pre["next"] = node
    linkedList["size"] += 1

def printList(linkedList):
    pre = linkedList["next"]
    for i in range(linkedList["size"]):
        print(pre["data"])
        pre =pre["next"]

linkedList = {"size" : 0 , "next" : None}
insertNode(linkedList , 10)
insertNode(linkedList , 20)
insertNode(linkedList , 30)
insertNode(linkedList , 40)
printList(linkedList)
