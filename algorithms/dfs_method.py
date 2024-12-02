def find_cycle(graph):
    def has_cycle(path):
        return path[-1] in path[:-1]

    for start_node in graph.nodes:
        paths = [[start_node]]  
        while paths:
            current_path = paths.pop(0)  

            if has_cycle(current_path):
                last_node_index = current_path.index(current_path[-1])
                return current_path[last_node_index:]

            last_node = current_path[-1]
            for neighbor in graph.neighbors(last_node):
                new_path = current_path + [neighbor]  
                paths.append(new_path)

    return None