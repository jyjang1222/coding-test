class Node:
    num = 0
    data = None
adj_list = [[3], [6, 10], [7, 11], [0, 6, 8], [13], [14],
            [1, 3, 8, 10, 11], [2, 11], [3, 6, 10, 12],
            [13], [1, 6, 8], [2, 6, 7], [8], [4, 9], [5]]
N = len(adj_list)  # 그래프 정점 수
visited = [False for x in range(N)]  # 방문되면 True로
CCList = []

def dfs(visited, i , cc):
    stack = []
    node = Node()
    node.num = 0
    node.data = adj_list[i]
    stack.append(node)
    visited[i] = True
    print(i, end=" ")
    cc.append(i)
    while True:
        pop = stack.pop(-1)
        start = pop.num
        end = len(pop.data)

        for i in range(start, end):
            pop.num += 1
            if visited[pop.data[i]] is False:
                cc.append(pop.data[i])
                visited[pop.data[i]] = True
                print(pop.data[i], end=" ")
                stack.append(pop)
                node = Node()
                node.num = 0
                node.data = adj_list[pop.data[i]]
                stack.append(node)

                break
        if len(stack) == 0:
            return cc
            break

for i in range(N):

    if visited[i] is False:
        cc = []
        cc = dfs(visited, i , cc)
        CCList.append(cc)
print()
print("--------------------")
print(visited)
print(CCList)