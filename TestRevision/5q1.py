from adjacency_list import *

def distance_matrix(adj_lst):
    n = len(adj_lst)
    distance = [[float('inf') for _ in range(n)] for i in range(n)]
    for i in range(n):
        distance[i][i] = 0
        for edge in adj_lst[i]:
            distance[i][edge[0]] = edge[1]
        
    
    return distance

#graph_str = """\
#U 3 W
#0 1 5
#2 1 7
#"""

#adj_list = adjacency_list(graph_str)
#print(distance_matrix(adj_list))

## more readable output (less readable code):
#print("\nEach row on a new line:")
#print("\n".join(str(lst) for lst in distance_matrix(adj_list)))

graph_str = """\
D 2 W
0 1 4
"""

adj_list = adjacency_list(graph_str)
print(distance_matrix(adj_list))