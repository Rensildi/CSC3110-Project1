def bfs_cycle_detection(graph):
    def is_cycle(path):
        return len(path) > 1 and path[0] == path[-1]

    # Brute-force: Try all paths from each node
    for start_node in graph.nodes:
        paths = [[start_node]]  
        while paths:
            # Dequeue path from queue
            current_path = paths.pop(-1)  

            # Check if current path is a cycle
            if is_cycle(current_path):
                return current_path

            # Explore neighbors and add new paths to the queue
            last_node = current_path[-1]
            for neighbor in graph.neighbors(last_node):
                new_path = current_path + [neighbor]  
                paths.append(new_path)

    return None