from collections import deque

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
        if node1 not in self.adj[node2]:
            self.adj[node1].append(node2)
            self.adj[node2].append(node1)

    def number_of_nodes():
        return len()


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
