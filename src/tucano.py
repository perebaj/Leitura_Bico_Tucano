import networkx as  nx
import networkx.drawing as nx_drawing
import igraph
import pickle
import matplotlib.pyplot as plt
import numpy as np
from Utils import convert_igraph_to_nx
graph_ig = pickle.load(open('src/dados/Bico_tucano_02_scaled_binary_network.dat', 'rb'), encoding='latin1')
graph_ig.simplify()
# graph_ig = igraph.Graph.GRG(100, 0.2)
# igraph.summary(graph_ig)

edgelist = igraph.Graph.get_edgelist(graph_ig)
graph_nx = convert_igraph_to_nx(graph_ig)
print(graph_nx.number_of_edges())
print(graph_nx.number_of_nodes())

position_nodes = graph_ig.vs['pos_no']

# print(position_nodes[0:20])

position_dict_XY = {}
# position_dict_YZ = {}
# position_dict_ZX = {}


for x in range(graph_nx.number_of_nodes()):
    position_dict_XY[x] = position_nodes[x][0:2]
    # position_dict_YZ[x] = position_nodes[x][1:]
    # position_dict_ZX[x] = position_nodes[x][-1:1]
tucano_config = {

}
nx_drawing.draw_networkx(graph_nx, pos=position_dict_XY, node_size=1, font_size=1, width=0.5)
plt.show()