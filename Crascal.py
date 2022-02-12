import random
import networkx as nx

from itertools import combinations, groupby


def gnp_random_connected_graph(num_of_nodes: int,
                               completeness: int) -> list:
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
        
    return G, weight

def crascal(graph):
    vertexes=graph[0]
    weights=graph[1]
    edges = list(vertexes.edges())
    for i in range(len(edges)):
        edges[i]=[edges[i], weights[i]]        
    return edges


print(crascal(gnp_random_connected_graph(5,1)))