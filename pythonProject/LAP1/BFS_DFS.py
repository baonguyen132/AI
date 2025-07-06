import queue
import time

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


def order_bfs(graph , start_node):
    visited = set()
    order = []
    q = queue.Queue()
    q.put(start_node)

    while not q.empty():
        node = q.get()
        if(node not in visited):
            visited.add(node)
            order.append(node)
            for neighbour in graph[node]:
                if neighbour not in visited: q.put(neighbour)

    return order

def order_dfs(graph , start_node):
    visited = set()
    order = []

    stack = [start_node]
    while stack:
        node = stack.pop()
        if(node not in visited):
            order.append(node)
            visited.add(node)

            list = np.array(graph[node])
            list = np.flipud(list)
            for neighbour in list:
                if neighbour not in visited:  stack.append(neighbour)

    return order



def visualize_search(order , title , G , pos):
    plt.figure()
    plt.title(title)
    for i,node in enumerate(order , start=1):
        plt.clf()

        nx.draw(G, pos,with_labels=True , node_color= ['r' if n == node else 'b' for n in G.nodes ])
        plt.draw()
        plt.pause(0.5)
    plt.show()
    time.sleep(0.5)

G = nx.Graph()
G.add_edges_from([
    ('A' , 'B' ) , ('A' , 'C') , ('A' , 'D') ,
    ('B' , 'E') ,('B' , 'F') ,
    ('C' , 'G'), ('C' , 'H') ,
    ('G' , 'X') ,
])


pos = nx.spring_layout(G)

visualize_search(order_dfs(G , 'A') , "DFS" , G , pos)
# visualize_search(order_bfs(G , 'A') , "BFS" , G , pos)
