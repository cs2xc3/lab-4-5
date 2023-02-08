from graph import Graph, DFS3, BFS3

# Example graph in lab
graph = Graph(7)
graph.add_edge(1, 2)
graph.add_edge(1, 3)

graph.add_edge(2, 4)

graph.add_edge(3, 4)
graph.add_edge(3, 5)

graph.add_edge(4, 6)
graph.add_edge(4, 5)

DFS3(graph, 1)
BFS3(graph, 1)
