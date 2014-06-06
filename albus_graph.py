import networkx as nx
import matplotlib.pyplot as plt
import csv, ast

#Create graph
G = nx.MultiDiGraph(summary="Albus mutant gene regulatory network")

#Read edges list
edges = []
with open("albus_edges.tsv") as f:
    edges = f.readlines()

G = nx.parse_edgelist(edges)
#G = nx.read_edgelist('albus_edges.tsv', nodetype=str, delimiter='\t', data=(('weight',float),('IsDirected',bool),('Source',str)))
print G.edges()
for edge in G.edges():
    print G.get_edge_data(*edge)


#Read nodes list
with open("albus_nodes.tsv") as tsv:
    for line in csv.reader(tsv, delimiter="\t"):
    	G.add_node(line[0], ast.literal_eval(line[1]))

#remove nodes without edges
outdeg = G.degree()
to_remove = [n for n in outdeg if outdeg[n] == 0]
G.remove_nodes_from(to_remove)

#Draw the graph
nodes = []
print G.nodes(data=True)
for n,d in G.nodes_iter(data=True):
	if d['Color'] == "green":
		nodes.append(n)

pos = nx.graphviz_layout(G)
nx.draw_networkx_nodes(G, pos, nodelist=nodes, node_size=200, node_color='g', alpha=0.5)

nodes = []
for n,d in G.nodes_iter(data=True):
	if d['Color'] == "yellow":
		nodes.append(n)

nx.draw_networkx_nodes(G, pos, nodelist=nodes, node_size=200, node_color='y', alpha=0.5)

nodes = []
print G.nodes(data=True)
for n,d in G.nodes_iter(data=True):
	if d['Color'] == "gray":
		nodes.append(n)

nx.draw_networkx_nodes(G, pos, nodelist=nodes, node_size=200, node_color='b', alpha=0.5)

nx.draw_networkx_labels(G, pos, font_size=10)

colors=range(nx.number_of_edges(G))
edges=nx.draw_networkx_edges(G,pos, edge_cmap=plt.cm.Blues, edge_color=colors, width=2)

plt.axis('equal')
plt.show()