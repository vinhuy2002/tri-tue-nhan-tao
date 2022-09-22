def greedy(graph, start, end, cost, path):
    max = 0
    tmp = ''
    if (start != end):
        for i in graph[start]:
            if (max < graph[start][i]):
                max = graph[start][i]
                tmp = i
        cost = cost + max
        path.append(tmp)
    
    if (start == end):
        print("Greedy Path: ")
        print(path)
        print("Cost: ")
        print(cost)
    else:
        return greedy(graph, tmp, end, cost, path)

if __name__ == "__main__":
    graph ={'S': {'A': 3, 'D': 2},
            'A': {'B': 5, 'C': 10}, 
            'B': {'C': 2, 'E': 1}, 
            'C': {'G': 4}, 
            'D': {'B': 1, 'E': 4}, 
            'E': {'G': 3}}
    start = 'S'
    end = 'G'
    cost = 0
    path = ['S']
    greedy(graph, start, end, cost, path)
