#

class Node:
    num = 0
    data = None
adj_list = [
            [2, 1],
            [3, 0],
            [3, 0],
            [9, 8, 2, 1],
            [5],
            [7, 6, 4],
            [7, 5],
            [6, 5],
            [3],
            [3]]
N = len(adj_list)  # 그래프 정점 수
visited = [False for x in range(N)]  # 방문되면 True로
def dfs(visited , i):
    stack = []
    node = Node()
    node.num = 0
    node.data = adj_list[i]
    stack.append(node)
    visited[i] = True
    print(i , end=" ")
    while True:
        pop = stack.pop(-1)
        start = pop.num
        end = len(pop.data)
        for i in range(start, end):
            pop.num += 1
            if visited[pop.data[i]] is False:
                visited[pop.data[i]] = True
                print(pop.data[i], end=" ")
                stack.append(pop)
                node = Node()
                node.num = 0
                node.data = adj_list[pop.data[i]]
                stack.append(node)
                break
        if len(stack) == 0:
            break

for i in range(N):

    if visited[i] is False:
        dfs(visited, i)
print()
print("--------------------")
print(visited)