import numpy as np
import random
import matplotlib.pyplot as plt
import networkx as nx

# Tạo tọa độ các thành phố
points = {
    'Arad': (91, 492), 'Bucharest': (400, 327), 'Craiova': (253, 288), 'Drobeta': (165, 299),
    'Eforie': (562, 293), 'Fagaras': (305, 449), 'Giurgiu': (375, 270), 'Hirsova': (534, 350),
    'Iasi': (473, 506), 'Lugoj': (165, 379), 'Mehadia': (168, 339), 'Neamt': (406, 537),
    'Oradea': (131, 571), 'Pitesti': (320, 368), 'Rimnicu': (233, 410), 'Sibiu': (207, 457),
    'Timisoara': (94, 410), 'Urziceni': (456, 350), 'Vaslui': (509, 444), 'Zerind': (108, 531)
}

# Lấy tên các thành phố
cities = list(points.keys())
num_cities = len(cities)

edges = [
    (item, items) for i, item in enumerate(cities) for j, items in enumerate(cities)
    if i < j
]
G = nx.Graph()
G.add_edges_from(edges)



# Hàm tính khoảng cách giữa hai thành phố
def distance(city1, city2):
    x1, y1 = points[city1]
    x2, y2 = points[city2]
    return np.sqrt((x1 - x2)**2 + (y1 - y2)**2)


# Hàm tính tổng khoảng cách của một lộ trình
def total_distance(route):
    dist = sum(distance(route[i], route[i + 1]) for i in range(len(route) - 1))
    return dist + distance(route[-1], route[0])  # Về lại thành phố đầu tiên




# Tạo một cá thể ngẫu nhiên
def create_individual():
    individual = cities[:]
    random.shuffle(individual)
    return individual


# Hàm đánh giá mức độ thích nghi của cá thể (càng thấp càng tốt)
def fitness(individual):
    return 1 / total_distance(individual)


# Hàm chọn lọc cá thể dùng phương pháp xác suất tỷ lệ thuận
def selection(population, fitnesses):
    return random.choices(population, weights=fitnesses, k=2)


# Hàm lai ghép hai cá thể
def crossover(parent1, parent2):
    start, end = sorted(random.sample(range(num_cities), 2))
    child = [None] * num_cities
    child[start:end] = parent1[start:end]
    pos = end
    for city in parent2:
        if city not in child:
            child[pos % num_cities] = city
            pos += 1
    return child


# Hàm đột biến cá thể
def mutate(individual, mutation_rate=0.1):
    for i in range(num_cities):
        if random.random() < mutation_rate:
            j = random.randint(0, num_cities - 1)
            individual[i], individual[j] = individual[j], individual[i]


# Hàm khởi tạo và thực thi giải thuật di truyền
def genetic_algorithm(pop_size=100, generations=1000, mutation_rate=0.1):
    population = [create_individual() for _ in range(pop_size)]
    best_individual = None
    best_fitness = 0

    for gen in range(generations):
        # Đánh giá mức độ thích nghi của từng cá thể
        fitnesses = [fitness(individual) for individual in population]

        # Tìm cá thể tốt nhất
        max_fitness_index = np.argmax(fitnesses)
        if fitnesses[max_fitness_index] > best_fitness:
            best_fitness = fitnesses[max_fitness_index]
            best_individual = population[max_fitness_index]

        # Sinh ra thế hệ mới
        new_population = []
        for _ in range(pop_size // 2):
            parent1, parent2 = selection(population, fitnesses)
            child1, child2 = crossover(parent1, parent2), crossover(parent2, parent1)
            mutate(child1, mutation_rate)
            mutate(child2, mutation_rate)
            new_population.extend([child1, child2])

        population = new_population

        # In ra quá trình tiến hóa
        if gen % 50 == 0:
            print(f"Generation {gen}: Best Distance = {1 / best_fitness:.2f}")

    return best_individual, 1 / best_fitness


# Thực thi giải thuật di truyền
best_route, best_distance = genetic_algorithm()
print("Best route:", best_route)
print("Best distance:", best_distance)


def drawGraph(path, title, G, pos):
    plt.figure(figsize=(10, 8))
    plt.title(title)

    # Vẽ các node thành phố
    nx.draw_networkx_nodes(G, pos, node_color='g', node_size=500)
    nx.draw_networkx_labels(G, pos, font_size=12, font_color='black')

    # Vẽ chỉ các đường thuộc lộ trình tốt nhất
    for i in range(len(path)):
        start_city = path[i]
        end_city = path[(i + 1) % len(path)]  # Quay lại thành phố đầu tiên
        x_coords = [pos[start_city][0], pos[end_city][0]]
        y_coords = [pos[start_city][1], pos[end_city][1]]
        plt.plot(x_coords, y_coords, 'r-', linewidth=2)

    plt.grid(True)
    plt.show()

# Vẽ đồ thị sau khi tìm ra lộ trình tối ưu
pos = nx.spring_layout(G)  # Vị trí của các node trong đồ thị
drawGraph(best_route, "Best Route", G, pos)

