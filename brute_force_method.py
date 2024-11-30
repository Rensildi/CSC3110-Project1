''' 
CSC 3110: Algorithm Design and Analysis
Group Members:  Parsa Nematollahe, 
                Imad Hoballah, 
                Hashir Ahmad, 
                Rensildi Kalanxhi
Project 3 - Description:
Given a set of vertices, and a set of edges in an adjacency matrix, determine the existing cycle in a
directed graph.

Assume there is always one and only one cycle.

Example:

Input -> Vertices (as an array of strings within the program)

vertices = { 'A', 'B', 'C', 'D', 'E'}

Adjacency matrix (as a bi-dimensional array within the program)

-999 is a value that represents infinity.

matrix=
{
-999  18   14  -999 16
-999 -999 -999  10  -999
-999  13  -999 -999 -999
-999 -999 -999 -999  11
-999 -999  17  -999 -999
}

Output:

Cycle vertices (as an array of strings within the program)
vertices = { ‘B’, ‘C’, ‘D’, ‘E’}

Also, notice the vertex list is not a set (where member order is not relevant) but a sequence (where
order matters).
'''
import networkx as nx
import matplotlib.pyplot as plt
import random

''' Brute Force Method O(2^n)'''
def brute_force_cycle_detection(graph):
    def check_path(path):
        
        if path[-1] in path[:-1]:
            
            cycle_start = path.index(path[-1])
            return path[cycle_start:]
        return None

    # Brute-force: Try all paths from each node
    for start_node in graph.nodes:
        paths = [[start_node]]  
        while paths:
            current_path = paths.pop(0)  
            last_node = current_path[-1]  

            # Check if current path contains a cycle
            cycle = check_path(current_path)
            if cycle: 
                return cycle

            # Explore neighbors and add new paths to the queue
            for neighbor in graph.neighbors(last_node):
                new_path = current_path + [neighbor]  
                paths.append(new_path)

    return None  

# Create a directed graph and add vertices
G = nx.DiGraph()
vertices = ['A', 'B', 'C', 'D', 'E']
G.add_nodes_from(vertices)

num_edges = random.randint(6, 6)
edges = random.sample([(u, v) for u in vertices for v in vertices if u != v], num_edges)
G.add_edges_from(edges)

cycle = brute_force_cycle_detection(G)

if cycle:
    title = "Cycle detected"
    cycle_edges = [(cycle[i], cycle[i+1]) for i in range(len(cycle)-1)] + [(cycle[-1], cycle[0])]
    edge_colors = ['red' if edge in cycle_edges else 'black' for edge in G.edges()]
    info_text = f"Cycle detected: {cycle}\nEdges: {edges}"
else:
    title = "No cycle detected"
    edge_colors = ['black'] * len(G.edges())
    info_text = f"No cycle detected\nEdges: {edges}"

# Plot the graph with limited size
plt.figure(figsize=(6, 6))  
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=15, font_weight='bold', edge_color=edge_colors, arrows=True)

plt.title(title)

plt.subplots_adjust(bottom=0.25)  
plt.figtext(0.5, 0.1, info_text, wrap=True, horizontalalignment='center', fontsize=10, bbox=dict(facecolor='white', alpha=0.7))  # Centered text below


plt.show()
