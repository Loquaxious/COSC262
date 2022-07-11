def min_capacity(city_map, depot_position):
    """Takes a map of a city and the position of the depot and returns the
    minimum battery capacity required to meet the above-mentioned
    criteria"""
    
    max_dist = 0
    
    adj_lst = adjacency_list(city_map)
    parent, distance = dijkstra(adj_lst, depot_position)
    
    for i in range(len(adj_lst)):
        if parent[i] != None:
            if max_dist < distance[i]:
                max_dist = distance[i]
    
    return int((((max_dist*3)*2)*6)/0.8)
    

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
U 4 W
0 2 5
0 3 2
3 2 2
"""

print(min_capacity(city_map, 0))
print(min_capacity(city_map, 1))
print(min_capacity(city_map, 2))