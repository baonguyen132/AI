import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

nodes = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]
neighbors = {
    "WA": ["NT", "SA"],
    "NT": ["WA", "SA", "Q"],
    "SA": ["WA", "NT", "Q", "NSW", "V"],
    "Q": ["NT", "SA", "NSW"],
    "NSW": ["Q", "SA", "V"],
    "V": ["SA", "NSW"],
    "T": []
}
colors = ["red", "green", "blue"]

for node in nodes:
    G.add_node(node)
    for neighbor in neighbors[node]:
        G.add_edge(node, neighbor)

def is_safe(node, color, color_assignment):
    for neighbor in neighbors[node]:
        if color_assignment.get(neighbor) == color:
            return False

    return True

def backtracking(index=0 ,color_assignment={}):
    if index == len(nodes):
        return True

    node = nodes[index]

    for color in colors:
        if is_safe(node, color, color_assignment):
            color_assignment[node] = color
            if backtracking(index + 1, color_assignment):
                return color_assignment
            color_assignment[node] = None

    return False


def draw(title ,G, pos):
    color_assignment = backtracking()
    print(color_assignment)

    plt.figure()
    nx.draw(G, pos, with_labels=True, node_color=[color_assignment[node] for node in nodes], node_size=2000,
            font_size=16, font_color="black", edge_color="black", linewidths=1, font_weight="bold")
    plt.title(title)
    plt.show()


pos = nx.spring_layout(G, seed=42)  # Sắp xếp vị trí các nút
draw("Chay" , G , pos)