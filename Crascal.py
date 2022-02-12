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
    set_of_vertex=set()
    for item in edges:
        for number in item[0]:
            set_of_vertex.add(number)
    list_of_sets=[]
    for item in set_of_vertex:
        list_of_sets.append({item})
    print(list_of_sets)
    edges = sorted(edges, key=lambda x: x[1])
    ver=[tuple(i[0]) for i in edges]
    # print(ver)
    

    tree=[edges[0][0]]  
    edges.pop(0)
    # print(edges)
    while len(list_of_sets)!=1:
        for k in range(len(ver)):
            tree.append(ver[k])
            for i in range(len(list_of_sets)):
                try:
                    if tree[-1][0] in list_of_sets[i] and tree[-1][1] not in list_of_sets[i]:
                        list_of_sets[i].add(tree[-1][1])
                        for j in range(len(list_of_sets)):
                            if tree[-1][1] in list_of_sets[j] and i!=j:
                                list_of_sets.pop(j)
                                # print(list_of_sets)
                                # print(ver[k])
                    else:
                        tree.remove(ver[k])
                except:
                    break
                    

    print(list_of_sets)



    # print(list_of_sets)
    return tree

    


print(crascal(gnp_random_connected_graph(5,1)))