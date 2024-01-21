import networkx as nx
import matplotlib.pyplot as plt

# Створення направленого графа
DG = nx.DiGraph()

# Додавання 15 вершин
for i in range(1, 16):
    DG.add_node(i)

# Додавання направлених ребер з вагою
weighted_edges = [
    (1, 2, 1),
    (1, 3, 2),
    (2, 4, 3),
    (2, 5, 2),
    (3, 6, 3),
    (4, 7, 1),
    (5, 7, 2),
    (6, 8, 1),
    (7, 9, 2),
    (8, 10, 3),
    (9, 10, 1),
    (1, 10, 4),
    (3, 7, 2),
    (5, 11, 2),
    (11, 12, 1),
    (12, 13, 3),
    (13, 14, 2),
    (14, 15, 1),
    (15, 1, 3),
    (10, 14, 4),
    (13, 15, 2),  # Додавання нового ребра між 13 та 15 вершинами
]
DG.add_weighted_edges_from(weighted_edges)

# Фіксація позицій вершин
fixed_positions = {
    1: (0.1, 0.9),
    2: (0.2, 0.7),
    3: (0.1, 0.5),
    4: (0.3, 0.9),
    5: (0.3, 0.7),
    6: (0.1, 0.3),
    7: (0.3, 0.5),
    8: (0.1, 0.1),
    9: (0.3, 0.3),
    10: (0.2, 0.1),
    11: (0.4, 0.9),
    12: (0.5, 0.7),
    13: (0.4, 0.5),
    14: (0.5, 0.3),
    15: (0.4, 0.1),
}

# Візуалізація направленого графа
plt.figure(figsize=(12, 10))
nx.draw(
    DG,
    fixed_positions,
    with_labels=True,
    node_color="lightgreen",
    node_size=800,
    font_size=15,
    font_weight="bold",
)
nx.draw_networkx_edge_labels(
    DG, fixed_positions, edge_labels=nx.get_edge_attributes(DG, "weight")
)
plt.title("Фіксований направлений граф транспортної мережі міста (15 вершин)")
plt.show()

# Вибір початкової вершини для алгоритмів
start_node = 1

# DFS (обхід у глибину)
dfs_path = list(nx.dfs_edges(DG, source=start_node))

# BFS (обхід у ширину)
bfs_path = list(nx.bfs_edges(DG, source=start_node))

# Виведення результатів DFS та BFS
print("DFS Path:", dfs_path)
print("BFS Path:", bfs_path)
