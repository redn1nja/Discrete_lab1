"""
Module visualizing Prim's and Kruskal's minimum spanning tree generation algorithms
"""


from prim import generate_mst_prim
from kruskal import generate_mstp_kruskal
from graph_gen import gnp_random_connected_graph

import networkx as nx
from networkx.algorithms import minimum_spanning_tree
import matplotlib.pyplot as plt

from time import perf_counter
import tqdm


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

