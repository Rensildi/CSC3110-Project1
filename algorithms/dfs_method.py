def dfs_cycle_detection(graph):
    def is_cycle(path):
        return len(path) > 1 and path[0] == path[-1]

    for start_node in graph.nodes:
        paths = [[start_node]]  
        while paths:
            current_path = paths.pop(0)  

            if is_cycle(current_path):
                return current_path

            last_node = current_path[-1]
            for neighbor in graph.neighbors(last_node):
                new_path = current_path + [neighbor]  
                paths.append(new_path)

    return None