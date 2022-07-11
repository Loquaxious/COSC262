def which_segments(city_map):
    """Takes the map of the city and returns a list of road segments that must 
    be cleared so that there is a clear path between any two locations and the 
    total length of the cleaned-up road segments in minimised"""
    result = []
    
    adj_lst = adjacency_list(city_map)
    parent, distance =  prim(adj_lst, 0)
    
    for i in range(1, len(adj_lst)):
        if parent[i] < i:
            result.append((parent[i],i))
        else:
            result.append((i,parent[i]))
    
    return result
    
def prim(adj_lst, start):
    """Prims minimum spanning tree algorithm"""
    n = len(adj_lst)
    in_tree = [False for _ in range(n)]
    distance = [float('inf') for _ in range(n)]
    parent = [None for _ in range(n)]
    distance[start] = 0
    while not all(in_tree):
        u = next_vertex(in_tree, distance)
        in_tree[u] = True
        for v, weight in adj_lst[u]:
            if not in_tree[v] and weight < distance[v]:
                distance[v] = weight
                parent[v] = u
    return parent, distance

        
        
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
    
    
def adjacency_list(graph_str):
    """Takes the textual representation of a graph and returns
    the adjacency list representation"""
    char_lst = []
    split_str = graph_str.splitlines()
    for line in split_str:
        char_lst.append(line.split())
        
    vertices = int(char_lst[0][1])
    result = [[] for _ in range(vertices)]  
    
    for edge in char_lst[1:]:
        result[int(edge[0])].append((int(edge[1]), int(edge[2])))
        result[int(edge[1])].append((int(edge[0]), int(edge[2])))
    
    return result 


city_map = """\
U 3 W
0 1 1
2 1 2
2 0 4
"""

print(sorted(which_segments(city_map)))

city_map = """\
U 1 W
"""

print(sorted(which_segments(city_map)))

city_map = """\
U 4 W
0 1 3
0 2 1
2 1 2
2 3 3
3 1 2
3 0 1
"""

print(sorted(which_segments(city_map)))