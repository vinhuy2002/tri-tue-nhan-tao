import collections
from collections import defaultdict

def createGraph():
    canh=[
        ["a", "b"], ["a", "g"], ["b", "c"], ["b", "g"],
        ["g", "l"], ["g", "h"], ["c", "h"], ["h", "i"],
        ["h", "m"], ["m", "i"], ["i", "d"], ["i", "e"],
        ["i", "j"], ["i", "n"], ["d", "e"], ["e", "j"],
        ["e", "f"], ["f", "k"], ["j", "k"], ["j", "n"]
    ]
    graph= defaultdict(list)
    for i in canh:
        a,b = i[0], i[1]
        graph[a].append(b)
        graph[b].append(a)
    return graph

def bfs(graph, root):

    visited, queue = set(), collections.deque([root])
    visited.add(root)

    while queue:
        vertex = queue.popleft()
        print(str(vertex) + " ", end="")
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

if __name__ == '__main__':
    graph = createGraph()
    print("Breadth First Traversal: ")
    bfs(graph, "a")