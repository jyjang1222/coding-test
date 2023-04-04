# https://gmlwjd9405.github.io/2018/08/27/algorithm-topological-sort.html

def setCount(adj_list , count_of_link , size):
    print(count_of_link)
    for i in range(size):
        for n in range(len(adj_list[i])):
            index = adj_list[i][n]
            count_of_link[index]  +=1

    print(count_of_link)

    queue = []

    for i in range(size):
        if count_of_link[i] == 0:
            queue.append(i)

    for n in range(size):
        if len(queue) == 0:
            break
        v = queue.pop()
        print("v : ", v, end=" ")
        for j in adj_list[v]:
            count_of_link[j] -= 1
            if count_of_link[j] == 0:
                queue.append(j)
        print(count_of_link)



adj_list = [[2, 3], [3,4], [3,5], [5], [5],[]]

size = len(adj_list)  # 그래프 정점 수
count_of_link = [0 for x in range(size)]  # 방문되면 True로


setCount(adj_list , count_of_link , size)