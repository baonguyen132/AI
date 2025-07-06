graph = {
    'A': ['B' , 'C' , 'D'],
    'B': ['E' , 'F'],
    'C': ['G' , 'H'],
    'D': [],
    'E': [],
    'F': [],
    'G': ['X'],
    'H': [],
    'X': []
}

def search(visited, end):
    visited.reverse()
    s = end
    for vertex in visited:
        if (end in graph[vertex]):
            s = str(vertex) + "->" + s
            end = vertex

    print(s)

def bfs(graph, start , end):
    visited = []
    queue = [start]

    while queue:
        node = queue.pop(0)
        for vertex in graph[node]:
            if vertex not in visited: queue.append(vertex)
        visited.append(node)

    search(visited, end)

if __name__ == '__main__':
    bfs(graph, 'A' , 'X')