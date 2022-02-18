import random
from time import perf_counter
import networkx as nx
from networkx.algorithms import minimum_spanning_tree
from itertools import combinations, groupby
import matplotlib.pyplot as plt


def gnp_random_connected_graph(num_of_nodes: int, completeness: int) -> nx.Graph:
    """
    Generates a random undirected graph, similarly to an Erdős-Rényi
    graph, but enforcing that the resulting graph is conneted
    """
    edges = combinations(range(num_of_nodes), 2)
    G = nx.Graph()
    G.add_nodes_from(range(num_of_nodes))
    for _, node_edges in groupby(edges, key=lambda x: x[0]):
        node_edges = list(node_edges)
        random_edge = random.choice(node_edges)
        G.add_edge(*random_edge)
        for e in node_edges:
            if random.random() < completeness:
                G.add_edge(*e)

    for (u, v, w) in G.edges(data=True):
        w['weight'] = random.randint(0, 10)

    return G


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


def visualize_mstp(G):
    plt.figure(1)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    weights = [(*data[0:2], data[2]["weight"]) for data in G.edges(data=True)]
    labels = {e[0:2]: e[2] for e in weights}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.figure(2)
    T = generate_mst_prim(G)
    pos = nx.spring_layout(T)
    nx.draw(T, pos, with_labels=True)
    weights = [(*data[0:2], data[2]["weight"]) for data in T.edges(data=True)]
    labels = {e[0:2]: e[2] for e in weights}
    nx.draw_networkx_edge_labels(T, pos, edge_labels=labels)

    plt.figure(3)
    M = minimum_spanning_tree(G)
    pos = nx.spring_layout(M)
    nx.draw(M, pos, with_labels=True)
    weights = [(*data[0:2], data[2]["weight"]) for data in M.edges(data=True)]
    labels = {e[0:2]: e[2] for e in weights}
    nx.draw_networkx_edge_labels(M, pos, edge_labels=labels)

    plt.show()


if __name__ == "__main__":
    G = gnp_random_connected_graph(20, 0.3)
    t = perf_counter()
    T = generate_mst_prim(G)
    t = perf_counter() - t
    print(t)
    visualize_mstp(G)
