from collections import deque
import random

# Undirected graph using an adjacency list
class Graph:
    def __init__(self, n):
        self.adj = {}
        for i in range(n):
            self.adj[i] = []

    def are_connected(self, node1, node2):
        return node2 in self.adj[node1]

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self):
        self.adj[len(self.adj)] = []

    def add_edge(self, node1, node2):
        if not self.are_connected(node1, node2):
            self.adj[node1].append(node2)
            self.adj[node2].append(node1)

    def remove_edge(self, node1, node2):
        self.adj[node1].remove(node2)
        self.adj[node2].remove(node1)

    def number_of_nodes():
        return len()

def create_random_graph(i: int, j: int) -> Graph:
    if (j > (i - 1) * i / 2):
        raise ValueError(f'Cannot create {j} unique edges for {i} nodes')

    E = Graph(i)
    G = Graph(i)

    for node_a in range(i):
        for node_b in range(node_a + 1, i):
            E.add_edge(node_a, node_b)

    unsaturated_nodes = [n for n in range(i)]

    while j > 0:
        node_a = random.choice(unsaturated_nodes)

        if len(E.adj[node_a]) == 0:
            unsaturated_nodes.remove(node_a)
            continue

        node_b = random.choice(E.adj[node_a])
        G.add_edge(node_a, node_b)
        E.remove_edge(node_a, node_b)
        j -= 1

    return G


# Breadth First Search
def BFS(G, node1, node2):
    Q = deque([node1])
    marked = {node1: True}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if node == node2:
                return True
            if not marked[node]:
                Q.append(node)
                marked[node] = True
    return False


# Depth First Search
def DFS(G, node1, node2):
    S = [node1]
    marked = {}
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adj[current_node]:
                if node == node2:
                    return True
                S.append(node)
    return False


def BFS3(G, node):
    Q = deque([node])
    marked = {node: True}
    preDict = {}
    for n in G.adj:
        if n != node:
            marked[n] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for n in G.adj[current_node]:
            if not marked[n]:
                Q.append(n)
                marked[n] = True
                preDict[n] = current_node
    print(preDict)
    return preDict


def DFS3(G, node):
    S = [node]
    marked = {}
    preDict = {}
    for n in G.adj:
        marked[n] = False
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            for n in G.adj[current_node]:
                if not marked[n]:
                    preDict[n] = current_node
                S.append(n)
    print(preDict)
    return preDict
