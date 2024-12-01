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