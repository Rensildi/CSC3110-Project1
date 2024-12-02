def find_cycle(vertices, adjacency_matrix):
    
    def dfs(node, visited, stack):
        if node in stack:  # Cycle found
            cycle_start_index = stack.index(node)
            return stack[cycle_start_index:]  
        if visited[node]:  
            return None
        
        visited[node] = True
        stack.append(node)
        
        for neighbor in range(len(vertices)):
            if adjacency_matrix[node][neighbor] != -999:  
                cycle = dfs(neighbor, visited, stack)
                if cycle:
                    return cycle
        
        stack.pop()  
        return None

    # Initialize visited list and stack
    visited = [False] * len(vertices)
    stack = []
    
    # Start DFS from each vertex
    for start_node in range(len(vertices)):
        if not visited[start_node]:
            cycle = dfs(start_node, visited, stack)
            if cycle:
                return [vertices[i] for i in cycle]  # Convert indices to vertex labels
    
    return None  


# Example Input
vertices = ['A', 'B', 'C', 'D', 'E']
matrix = [
    [-999, 18, 14, -999, 16],
    [-999, -999, -999, 10, -999],
    [-999, 13, -999, -999, -999],
    [-999, -999, -999, -999, 11],
    [-999, -999, 17, -999, -999]
]

# Find the cycle
cycle = find_cycle(vertices, matrix)
print("Cycle vertices:", cycle)



""" 
DFS Function:

1: Starts at a vertex and recursively explores its neighbors.
2: Detects a cycle when a node is revisited within the current stack.
3: Backtracks when all neighbors of a node are visited.

Visited Array:
1: Keeps track of vertices already fully processed.

Stack:
1: Maintains the current path of exploration to reconstruct the cycle.

"""