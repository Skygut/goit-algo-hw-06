import networkx as nx
import matplotlib.pyplot as plt
import heapq


def dijkstra_path(graph, start, end):
    distances = {vertex: float("infinity") for vertex in graph}
    previous_vertices = {vertex: None for vertex in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        if current_vertex == end:
            break

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_vertices[neighbor] = current_vertex
                heapq.heappush(pq, (distance, neighbor))

    path, current_vertex = [], end
    while current_vertex is not None:
        path.insert(0, current_vertex)
        current_vertex = previous_vertices[current_vertex]

    return path if path[0] == start else []


DG = nx.DiGraph()

for i in range(1, 16):
    DG.add_node(i)

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
    (10, 14, 15),
    (13, 15, 2),
]
DG.add_weighted_edges_from(weighted_edges)

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


graph = {node: {} for node in DG.nodes()}
for u, v, weight in DG.edges(data="weight"):
    graph[u][v] = weight


shortest_path = dijkstra_path(graph, 1, 15)

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
plt.title("Граф транспортної мережі із 15 зупинками (вершинами)")
plt.show()

print("Найкоротший шлях від вершини 1 до вершини 15:", shortest_path)
