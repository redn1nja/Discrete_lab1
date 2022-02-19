import random
from matplotlib import container
import networkx as nx
import matplotlib.pyplot as plt
import time

from itertools import combinations, groupby

def gnp_random_connected_graph(num_of_nodes: int,
                               completeness: int,
                               draw: bool = False):
    """
    Generates a random undirected graph, similarly to an Erdős-Rényi 
    graph, but enforcing that the resulting graph is conneted
    """
    weight = []

    edges = combinations(range(num_of_nodes), 2)
    G = nx.Graph()
    G.add_nodes_from(range(num_of_nodes))
    
    for _, node_edges in groupby(edges, key = lambda x: x[0]):
        node_edges = list(node_edges)
        random_edge = random.choice(node_edges)
        G.add_edge(*random_edge)
        for e in node_edges:
            if random.random() < completeness:
                G.add_edge(*e)
                
    for (u,v,w) in G.edges(data=True):
        w['weight'] = random.randint(0,10)
        weight.append(w['weight'])
                
    if draw: 
        plt.figure(figsize=(10,6))
        nx.draw(G, node_color='lightblue', 
            with_labels=True, 
            node_size=500)
    
    return G, weight



def kruskal(graph: list):
    indx_v1 = 0
    indx_v2 = 0
    G = graph[0]
    edges = list(G.edges())
    nodes = list(G.nodes())
    weights = graph[1]
    container_for_union = []
    lst_edges_tree = []
    graph = list(zip(edges, weights))
    graph = sorted(graph, key = lambda x: x[-1])

    list_of_vertexes = []
    st_container = set()
    for node in nodes:
        st_container.add(str(node))
        list_of_vertexes.append(st_container)
        st_container = set()
    for i in range(0, len(graph)):
        graph[i] = tuple(str(y) for  y in graph[i][0])
        v1 = graph[i][0]
        v2 = graph[i][1]
        for v in range(len(list_of_vertexes)):
            if v1 in list_of_vertexes[v] and v2 in list_of_vertexes[v]:
                break
            if v1 in list_of_vertexes[v]:
                indx_v1 = v
                container_for_union.append(list_of_vertexes[indx_v1])
            if v2 in list_of_vertexes[v]:
                indx_v2 = v
                container_for_union.append(list_of_vertexes[indx_v2])
            if len(container_for_union) == 2:
                good_edge = tuple(int(vertex) for vertex in graph[i])
                lst_edges_tree.append(good_edge)
                to_add = []
                to_add.append(container_for_union[0].union(container_for_union[1]))
                list_of_vertexes.append(to_add[0])
                container_for_union = []
                if indx_v1 > indx_v2:
                    list_of_vertexes.pop(indx_v1)
                    list_of_vertexes.pop(indx_v2)
                else:
                    list_of_vertexes.pop(indx_v2)
                    list_of_vertexes.pop(indx_v1)
                break

    return lst_edges_tree

# if __name__== "__main__":
    # time_taken = 0
    # for i in range(10):
        # start = time.time()
        # kruskal(gnp_random_connected_graph(500, 1))
        # end = time.time()
        # time_taken += (end-start)
    # print(time_taken)
    # print(time_taken/10)
