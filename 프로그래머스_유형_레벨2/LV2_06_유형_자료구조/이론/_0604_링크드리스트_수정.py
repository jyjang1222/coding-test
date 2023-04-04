def updateNode(linkedList, index, value):
    if linkedList["size"] <= index:
        return
    if index == 0:
        linkedList["next"]["data"] = value
    else:
        pre = linkedList["next"]
        for i in range(index):
            pre = pre["next"]
        pre["data"] = value


def removeNode(linkedList, index):
    if linkedList["size"] <= index:
        return
    if linkedList["size"] == 0:
        return
    if linkedList["size"] == 1:
        remove = linkedList["next"]
        linkedList["next"] = None
        linkedList["size"] -= 1
        return remove
    else:
        if index == 0:
            remove = linkedList["next"]
            linkedList["next"] = remove["next"]
            remove["next"] = None
            linkedList["size"] -= 1
            return remove
        else:
            pre = linkedList["next"]
            for i in range(index - 1):
                pre = pre["next"]
            remove = pre["next"]
            pre["next"] = remove["next"]
            remove["next"] = None
            linkedList["size"] -= 1
            return remove


def insertNode(linkedList, data):
    node = {"data": data, "next": None}
    if linkedList["size"] == 0:
        linkedList["next"] = node
    else:
        pre = linkedList["next"]
        for i in range(linkedList["size"] - 1):
            pre = pre["next"]
        pre["next"] = node
    linkedList["size"] += 1


def printList(linkedList):
    pre = linkedList["next"]
    for i in range(linkedList["size"]):
        print(pre["data"])
        pre = pre["next"]


linkedList = {"size": 0, "next": None}
insertNode(linkedList, 10)
insertNode(linkedList, 20)
insertNode(linkedList, 30)
insertNode(linkedList, 40)
# a = removeNode(linkedList , 2)
# print(a)
updateNode(linkedList, 2, 100)

printList(linkedList)
