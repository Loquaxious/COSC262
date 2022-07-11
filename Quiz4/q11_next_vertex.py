def next_vertex(in_tree, distance):
    """Takes two arrays and returns the vertex that should be added
    to the tree next"""
    n = len(in_tree)
    next_vertex = None
    current_min = None
    
    for vertex in range(n):
        if not in_tree[vertex]:
            if current_min == None: 
                current_min = distance[vertex]
                next_vertex = vertex
            else:
                if distance[vertex] < current_min:
                    current_min = distance[vertex]
                    next_vertex = vertex
    return next_vertex
                    

from math import inf
in_tree = [False, True, True, False, False]
distance = [float('inf'), 0, 3, 12, 5]
print(next_vertex(in_tree, distance))

in_tree = [False, False, False]
distance = [float('inf'), 0, float('inf')]
print(next_vertex(in_tree, distance))