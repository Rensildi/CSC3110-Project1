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

''' DFS method O(n)'''
def dfs_cycle_detection(graph):
    def dfs(node, visited, rec_stack):
        visited[node] = True
        rec_stack[node] = True
        
        for neighbor in graph.neighbors(node):
            if not visited[neighbor] and dfs(neighbor, visited, rec_stack):
                return True
            elif rec_stack[neighbor]:
                return True
        
        rec_stack[node] = False
        return False
    
    visited = {node: False for node in graph.nodes}
    rec_stack = {node: False for node in graph.nodes}
    
    for node in graph.nodes:
        if not visited[node]:
            if dfs(node, visited, rec_stack):
                return True
    return False

''' Creating the graph test'''
G = nx.DiGraph()
vertices = ['A', 'B', 'C', 'D', 'E']
G.add_nodes_from(vertices)

edges = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'B')]
G.add_edges_from(edges)

cycle_detected = dfs_cycle_detection(G)

plt.figure(figsize=(6, 6))  
pos = nx.spring_layout(G) 

edge_colors = ['red' if cycle_detected else 'black'] * len(G.edges())
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=15, font_weight='bold', edge_color=edge_colors, arrows=True)

''' Texts in the graph coordinations '''
if cycle_detected:
    title = "Cycle detected"
    info_text = "A cycle exists in the graph."
else:
    title = "No cycle detected"
    info_text = "No cycle found in the graph."

plt.title(title)
plt.subplots_adjust(bottom=0.25)
plt.figtext(0.5, 0.1, info_text, wrap=True, horizontalalignment='center', fontsize=10, bbox=dict(facecolor='white', alpha=0.7))


plt.show()
