import time

import networkx as nx
import matplotlib.pyplot as plt
import math
import queue


G = nx.Graph()
G.add_weighted_edges_from([
    ('Arad','Sibiu', 140.0), ('Arad','Zerind', 75.0), ('Arad','Timisoara', 118.0),
    ('Zerind','Arad', 75.0), ('Zerind','Oradea', 71.0),
    ('Oradea','Zerind', 71.0), ('Oradea','Sibiu', 151.0),
    ('Sibiu','Arad', 140.0), ('Sibiu','Oradea', 151.0), ('Sibiu','Fagaras', 99.0), ('Sibiu','Rimnicu', 80.0),
    ('Timisoara','Arad', 118.0), ('Timisoara','Lugoj', 111.0),
    ('Lugoj','Timisoara', 111.0), ('Lugoj','Mehadia', 70.0),
    ('Mehadia','Lugoj', 70.0), ('Mehadia','Drobeta', 75.0),
    ('Drobeta','Mehadia', 75.0), ('Drobeta','Craiova', 120.0),
    ('Craiova','Drobeta', 120.0), ('Craiova','Rimnicu', 146.0), ('Craiova','Pitesti', 138.0),
    ('Rimnicu','Sibiu', 80.0), ('Rimnicu','Craiova', 146.0), ('Rimnicu','Pitesti', 97.0),
    ('Fagaras','Sibiu', 99.0), ('Fagaras','Bucharest', 211.0),
    ('Pitesti','Rimnicu', 97.0), ('Pitesti','Craiova', 138.0), ('Pitesti','Bucharest', 101.0),
    ('Bucharest','Fagaras', 211.0), ('Bucharest','Pitesti', 101.0), ('Bucharest','Giurgiu', 90.0), ('Bucharest','Urziceni', 85.0),
    ('Giurgiu','Bucharest', 90.0),
    ('Urziceni','Bucharest', 85.0), ('Urziceni','Vaslui', 142.0), ('Urziceni','Hirsova', 98.0),
    ('Hirsova','Urziceni', 98.0), ('Hirsova','Eforie', 86.0),
    ('Eforie','Hirsova', 86.0),
    ('Vaslui','Iasi', 92.0), ('Vaslui','Urziceni', 142.0),
    ('Iasi','Vaslui', 92.0), ('Iasi','Neamt', 87.0),
    ('Neamt','Iasi', 87.0)
])

point = [
    {
        'Arad': (91, 492),
        'Bucharest': (400, 327),
        'Craiova': (253, 288),
        'Drobeta': (165, 299),
        'Eforie': (562, 293),
        'Fagaras': (305, 449),
        'Giurgiu': (375, 270),
        'Hirsova': (534, 350),
        'Iasi': (473, 506),
        'Lugoj':(165, 379),
        'Mehadia': (168, 339),
        'Neamt': (406, 537),
        'Oradea': (131, 571),
        'Pitesti': (320, 368),
        'Rimnicu': (233, 410),
        'Sibiu': (207, 457),
        'Timisoara': (94, 410),
        'Urziceni': (456, 350),
        'Vaslui': (509, 444),
        'Zerind': (108, 531)
    }
]

def drawGraph (path,title ,G, pos) :
    plt.figure()
    for i, node in enumerate(path , start=1):
        plt.clf()
        plt.title(title)
        nx.draw(G, pos, with_labels=True, node_color=['r' if n == node else 'g' for n in G.nodes])

        plt.draw()
        plt.pause(0.5)

    plt.show()
    time.sleep(.5)

def heuristic(namePoint1, namePoint2):
    x1 = point[0].get(namePoint1)[0]
    x2 = point[0].get(namePoint2)[0]

    y1 = point[0].get(namePoint1)[1]
    y2 = point[0].get(namePoint2)[1]

    giatri = math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2))
    return round(giatri , 2)

def greedy(G,node_start, node_end):
    frontier = queue.PriorityQueue()
    frontier.put((heuristic(node_start, node_end), node_start))
    paths = []
    visited = set()

    while not frontier.empty():
        node = frontier.get()
        paths.append(node)

        if node[1] == node_end: break
        for neighbor in G.neighbors(node[1]):
            if neighbor not in visited:
                frontier.put((heuristic(neighbor, node_end), neighbor))

    path = []
    total_cost = 0
    for item in paths:
        path.append(item[1])
        total_cost+=item[0]
    print(paths)
    print("Tổng chi phí: ", total_cost)
    return path


pos = nx.spring_layout(G)

drawGraph(greedy(G , "Oradea" , "Pitesti"), "Graph", G , pos)
