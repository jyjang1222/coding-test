
def printList(linkedList):
    pre = linkedList["next"]
    for i in range(linkedList["size"]):
        print(pre["data"])
        pre =pre["next"]



linkedList = {"size" : 0 , "next" : None}
node1 = {"data" : 1, "next" : None}
node2 = {"data" : 2 , "next" : None}
node3 = {"data" : 3 , "next" : None}
node1["next"] = node2
node2["next"] = node3
linkedList["size"] = 3
linkedList["next"] = node1
printList(linkedList)
