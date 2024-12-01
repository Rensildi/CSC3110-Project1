import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import string

from algorithms import dfs_method
from algorithms import bfs_method

def plot_graph_with_cycle(graph, cycle):
    if cycle:
        title = "Cycle detected"
        cycle_edges = [(cycle[i], cycle[i+1]) for i in range(len(cycle)-1)] + [(cycle[-1], cycle[0])]
        edge_colors = ['red' if edge in cycle_edges else 'black' for edge in graph.edges]
        info_text = f"Cycle detected: {cycle}\nEdges: {graph.edges}"
    else:
        title = "No cycle detected"
        edge_colors = ['black'] * len(graph.edges)
        info_text = f"No cycle detected\nEdges: {graph.edges}"

    plt.figure(figsize=(6, 6))  
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=15, font_weight='bold', edge_color=edge_colors, arrows=True)

    plt.title(title)

    plt.subplots_adjust(bottom=0.25)  
    plt.figtext(0.5, 0.1, info_text, wrap=True, horizontalalignment='center', fontsize=10, bbox=dict(facecolor='white', alpha=0.7))


    plt.show()

num_vertices = 6

# Create random adjacency matrix
adjacency_matrix = np.random.randint(2, size=(num_vertices, num_vertices))
# Ensure diagonal of adjacency matrix is 0
np.fill_diagonal(adjacency_matrix, 0)

G = nx.from_numpy_array(adjacency_matrix, create_using=nx.DiGraph)

# Relabel graph vertices from numbers to letters
vertices = list(string.ascii_uppercase[:num_vertices])
relabeling = {i: vertices[i] for i in range(len(vertices))}
G = nx.relabel_nodes(G, relabeling)

cycle = dfs_method.find_cycle_dfs(G)

plot_graph_with_cycle(G, cycle)
