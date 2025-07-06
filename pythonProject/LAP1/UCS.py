import time

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import queue



def ucs(graph , start_node , goal_node):
    frontier = queue.PriorityQueue()
    frontier.put((0 , start_node))

    came_from = {}
    cost_so_far = {}

    came_from[start_node] = None
    cost_so_far[start_node] = 0

    while not frontier.empty():
        node = frontier.get()

        if node[1] == goal_node : break
        for neighbor, weight  in graph[node[1]].items():
            new_cost = cost_so_far[node[1]] + weight["weight"]
            if neighbor not in came_from or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost
                frontier.put((priority , neighbor))
                came_from[neighbor] = node[1]

    path = []
    current = goal_node
    while current != None:
        path.insert(0, current)
        current = came_from[current]

    print(path)
    print(cost_so_far[goal_node])
    return path


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
pos = nx.spring_layout(G)

drawGraph(ucs(G , "Arad" , "Bucharest"),"Graph" , G , pos)

