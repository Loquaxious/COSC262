from adjacency_list import adjacency_list

def dijkstra(adj_list, start):
    """Takes a weighted adjacency list and a starting vertex the runs dijkstra's
    shortest path algorithm and returns a pair containing the parent and 
    distance arrays""" 
    n = len(adj_list)
    in_tree = [False for _ in range(n)]
    distance = [float('inf') for _ in range(n)]
    parent = [None for _ in range(n)]
    distance[start] = 0
    
    while not all(in_tree):
        u = next_vertex(in_tree, distance)
        in_tree[u] = True
        for v, weight in adj_list[u]:
            if not in_tree[v] and distance[u] + weight < distance[v]:
                distance[v] = distance[u] + weight
                parent[v] = u
    return (parent, distance)

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


#graph_string = """\
#D 3 W
#1 0 3
#2 0 1
#1 2 1
#"""

#print(dijkstra(adjacency_list(graph_string), 1))
#print(dijkstra(adjacency_list(graph_string), 2))

graph_string = """\
U 4 W
0 2 5
0 3 2
3 2 2
"""

print(dijkstra(adjacency_list(graph_string), 0))
print(dijkstra(adjacency_list(graph_string), 2))