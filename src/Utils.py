# -*- coding: utf-8 -*-

import networkx as nx
import igraph as ig
import numpy as np
import matplotlib.pyplot as plt
import igraph

def convert_networkx_to_igraph(graph_nx):
    # convert via adjacency matrix
    g2 = ig.Graph().Adjacency((nx.to_numpy_array(graph_nx) > 0).tolist())
    g2 = g2.as_undirected()
    return g2

def edgelist_nx(graph_nx):
    edgelist2 = []
    for line in graph_nx.edges():   edgelist2.append((line))
    print(line)

def convert_igraph_to_nx(graph_ig):
    graph_nx = nx.Graph() #intancia do grafo tipo networkx 
    graph_nx.add_nodes_from(np.arange(graph_ig.vcount())) #instancia do grafo com o mesmo número de nós de {graph_ig}
    edgelist = graph_ig.get_edgelist() #lista de arestas do grafo {graph_ig}
    graph_nx.add_edges_from(edgelist) #adiciona as areasta em {graph_nx}
    return graph_nx


def print_nx_graph(graph_nx):
    for line in nx.generate_adjlist(graph_nx):
        print(line)


def draw_nx(graph_nx):
    nx.draw(graph_nx, with_labels=True, font_weight='bold')
    plt.show()

def confimation(graph_ig, graph_nx):
    igraph.summary(graph_ig)
    print(graph_nx.number_of_edges())
    print(graph_nx.number_of_nodes())



