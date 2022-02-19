"""
Module implementing Prim's algorithm for minimum spanning tree generation
"""
import networkx as nx
from heapq import heappop, heappush


def generate_mst_prim(graph: nx.Graph) -> nx.Graph:
    """
    Generates the minimum spanning tree for a given graph using Prim algorithm.
    """
    tree = nx.Graph()
    push = heappush
    pop = heappop

    nodes = set(graph)
    tree.add_nodes_from(nodes)

    while nodes:
        u = nodes.pop()
        frontier = []
        visited = {u}
        for v, d in graph.adj[u].items():
            wt = d.get("weight", 1)
            push(frontier, (wt, u, v, d))
        while frontier:
            W, u, v, d = pop(frontier)
            if v in visited or v not in nodes:
                continue
            tree.add_edge(u, v, weight=W)
            visited.add(v)
            nodes.discard(v)
            for w, d2 in graph.adj[v].items():
                if w in visited:
                    continue
                new_weight = d2.get("weight", 1)
                push(frontier, (new_weight, v, w, d2))

    return tree
