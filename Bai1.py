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

def timDuong(graph, s, e):
    visited = set()
    visited.add(s)
    return __timDuong(graph, s, e, visited)

def __timDuong(graph, start, end, visited):
    if start == end:
        return [start]
    
    if start in graph:
        for i in graph[start]:
            if i not in visited:
                visited.add(i)
                duongDi = __timDuong(graph, i, end, visited)
                if duongDi is not None:
                    duongDi.insert(0, start)
                    return duongDi
    
    return None

if __name__ == "__main__":
    graph = createGraph()
    print(timDuong(graph, 'a', 'k'))