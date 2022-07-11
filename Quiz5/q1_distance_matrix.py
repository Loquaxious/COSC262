from adjacency_list import adjacency_list

def distance_matrix(adj_list):
    """Takes and adjacency list of a weighted graph and returns a distance 
    matrix that can be used as input for Floyd's algorithm"""
    n = len(adj_list)
    matrix = [[float('inf') for _ in range(n)] for _ in range(n)]
    count = 0;
    
    for row in matrix:
        row[count] = 0
        count += 1
    
    count = 0
    for vertex in adj_list:
        for edge in vertex:
            matrix[count][edge[0]] = edge[1]
        count+=1
    return matrix

graph_str = """\
U 3 W
0 1 5
2 1 7
"""

adj_list = adjacency_list(graph_str)
print(distance_matrix(adj_list))

# more readable output (less readable code):
print("\nEach row on a new line:")
print("\n".join(str(lst) for lst in distance_matrix(adj_list)))

graph_str = """\
D 2 W
0 1 4
"""

adj_list = adjacency_list(graph_str)
print(distance_matrix(adj_list))