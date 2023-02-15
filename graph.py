from collections import deque
import random
from typing import List

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

    def number_of_nodes(self):
        return len(self.adj)

    def copy(self):
        new_graph = Graph(0)
        new_graph.adj = [edges.copy() for edges in self.adj]
        return new_graph


# returns the maximum number of unique edges for a graph i nodes
def max_unique_edges(i: int, self_loops = False) -> int:
    if not self_loops:
        return (i - 1) * i // 2
    return i * (i + 1) // 2

def create_random_graph(i: int, j: int) -> Graph:
    if j > max_unique_edges(i):
        raise ValueError(f'Cannot create {j} unique edges for {i} nodes')

    E = Graph(i)
    G = Graph(i)

    for node_a in range(i):
        for node_b in range(node_a + 1, i):
            E.add_edge(node_a, node_b)

    unsaturated_nodes = [n for n in range(i)]

    while j > 0:
        node_a = random.choice(unsaturated_nodes)

        if len(E.adjacent_nodes(node_a)) == 0:
            unsaturated_nodes.remove(node_a)
            continue

        node_b = random.choice(E.adjacent_nodes(node_a))
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
        for node in G.adjacent_nodes(current_node):
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
            for node in G.adjacent_nodes(current_node):
                if node == node2:
                    return True
                S.append(node)
    return False

#Depth First search remembering path
def DFS2(G, node1, node2):
    S = [node1]
    marked = {}
    L = []
    downstep = []

    for node in G.adj:
        marked[node] = False

    while len(S) != 0:
        current_node = S.pop()
        L.append(current_node)
        downstep.append(G.adjacent_nodes(current_node))
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adj[current_node]:
                if node == node2:
                    L.append(node)
                    if L.count(node1) > 1:
                        return DFShelper(L, node1)
                    return L
                S.append(node)

# Breadth First Search remembering path
def BFS2(G, node1, node2):
    Q = deque([[node1]])
    marked = {node1 : True}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_path = Q.popleft()
        for node in G.adj[current_path[-1]]:
            if node == node2:
                current_path.append(node)
                return current_path
            if not marked[node]:
                next_path = current_path.copy()
                next_path.append(node)
                Q.append(next_path)
                marked[node] = True
    return []

def BFS3(G, node):
    Q = deque([node])
    marked = {node: True}
    preDict = {}
    for n in G.adj:
        if n != node:
            marked[n] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for n in G.adjacent_nodes(current_node):
            if not marked[n]:
                Q.append(n)
                marked[n] = True
                preDict[n] = current_node
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
            for n in G.adjacent_nodes(current_node):
                if not marked[n]:
                    preDict[n] = current_node
                S.append(n)
    return preDict


def is_connected(G: Graph) -> bool:
    if G.number_of_nodes() == 0:
        return True
    return len(BFS3(G, 0)) + 1 == G.number_of_nodes()


def has_cycle(G):
    # prospective list of nodes
    nodes = list(range(G.number_of_nodes()))
    while len(nodes) != 0:
        # if loops, there are multiple connected components
        S = [nodes[0]]
        marked = {}
        preDict = {}
        for n in G.adj:
            marked[n] = False
        while len(S) != 0:
            current_node = S.pop()
            if not marked[current_node]:
                marked[current_node] = True
                # node has been visited, is connected so removed
                nodes.remove(current_node)
                for n in G.adjacent_nodes(current_node):
                    # if node has been visited and another node connects to it, cycle exists
                    if nodes.count(n) == 0 and preDict[current_node] != n:
                        return True
                    if not marked[n]:
                        preDict[n] = current_node
                    S.append(n)
    return False

#Use the methods below to determine minimum vertex covers

def add_to_each(sets, element):
    copy = sets.copy()
    for set in copy:
        set.append(element)
    return copy

def power_set(set):
    if set == []:
        return [[]]
    return power_set(set[1:]) + add_to_each(power_set(set[1:]), set[0])

def is_vertex_cover(G, C):
    for start in G.adj:
        for end in G.adjacent_nodes(start):
            if not(start in C or end in C):
                return False
    return True

def MVC(G):
    nodes = [i for i in range(G.number_of_nodes())]
    subsets = power_set(nodes)
    min_cover = nodes
    for subset in subsets:
        if is_vertex_cover(G, subset):
            if len(subset) < len(min_cover):
                min_cover = subset
    return min_cover

# Approximations
def approx2(G):
    nodeSet = []
    while not is_vertex_cover(G, nodeSet):
        v = random.randint(0, G.number_of_nodes())
        while v in nodeSet:
            v = random.randint(0, G.number_of_nodes())
        nodeSet.append(v)
    print(nodeSet)
    return nodeSet

