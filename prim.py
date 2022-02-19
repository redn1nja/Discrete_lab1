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

    tree.add_nodes_from(graph)

    u = 0
    visited_nodes = {u}
    incidental_nodes = []

    for v, data in graph.adj[u].items():
        heappush(incidental_nodes, (data["weight"], u, v))

    while incidental_nodes:
        weight, u, v = heappop(incidental_nodes)

        if v in visited_nodes:
            continue

        tree.add_edge(u, v, weight=weight)

        visited_nodes.add(v)

        for w, data in graph.adj[v].items():
            if w in visited_nodes:
                continue
            heappush(incidental_nodes, (data["weight"], v, w))

    return tree
