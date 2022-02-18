"""
Module implementing Kruskal's algorithm for minimal spanning tree generation
"""
import networkx as nx


def generate_mst_prim(graph: nx.Graph) -> nx.Graph:
    """
    Generates the minimum spanning tree for a given graph using Prim algorithm.
    """
    tree = nx.Graph()

    tree.add_nodes_from(list(graph.nodes()))

    inf = float("inf")

    num_of_nodes = graph.number_of_nodes()

    adjacency_list = tuple(graph.adjacency())

    selected_nodes = {0}

    num_edges = 0

    while (num_edges < num_of_nodes - 1):
        min_edge = inf
        a = 0
        b = 0
        for m in range(num_of_nodes):
            if m in selected_nodes:
                for n in range(num_of_nodes):
                    if (n not in selected_nodes and n in adjacency_list[m][1]):
                        if min_edge > adjacency_list[m][1][n]["weight"]:
                            min_edge = adjacency_list[m][1][n]["weight"]
                            a = m
                            b = n
        tree.add_edge(a, b, weight=min_edge)
        selected_nodes.add(b)
        num_edges += 1

    return tree
