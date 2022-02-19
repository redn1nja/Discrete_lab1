"""Prim's algorithm"""
import random
from itertools import combinations, groupby
import networkx as nx
import matplotlib.pyplot as plt
import time


def gnp_random_connected_graph(num_of_nodes: int,
                               completeness: int,
                               draw: bool = False) -> list[tuple[int, int]]:
    """
    Generates a random undirected graph, similarly to an Erdős-Rényi 
    graph, but enforcing that the resulting graph is conneted
    """
    weight_list = []

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
        weight_list.append(w['weight'])

    if draw:
        plt.figure(figsize=(10, 6))
        nx.draw(G, node_color='lightblue',
                with_labels=True,
                node_size=500)

    return G, weight_list


def prim(graph_info: tuple):
    """
    Get minimum spanning tree using Prim's algorithm.
    """
    minimum_spanning_tree = []

    G = graph_info[0]
    edges = list(G.edges())
    nodes_unvisited = list(G.nodes())
    weight_list = graph_info.edges(data=True)
    graph = sorted(list(zip(edges, weight_list)), key=lambda x: x[1])

    nodes_visited = [nodes_unvisited[0]]
    del nodes_unvisited[0]

    while nodes_unvisited:
        for edge_weight in graph:
            edge = edge_weight[0]
            node_1 = edge[0]
            node_2 = edge[1]

            if node_1 in nodes_visited and node_2 in nodes_unvisited:
                minimum_spanning_tree.append(edge)
                graph.remove(edge_weight)
                nodes_visited.append(node_2)
                nodes_unvisited.remove(node_2)
                break

            elif node_2 in nodes_visited and node_1 in nodes_unvisited:
                minimum_spanning_tree.append(edge)
                graph.remove(edge_weight)
                nodes_visited.append(node_1)
                nodes_unvisited.remove(node_1)
                break

    return minimum_spanning_tree


# if __name__ == '__main__':
    # # random_graph = gnp_random_connected_graph(500, 0.6)
    # # minimum_tree = prim(random_graph)
    # # print(minimum_tree)

    # time_taken = 0
    # for i in range(10):
        # start = time.time()
        # prim(gnp_random_connected_graph(500, 1)[0])
        # end = time.time()
        # time_taken += (end-start)
    # print(time_taken)
    # # print(time_taken/10)
