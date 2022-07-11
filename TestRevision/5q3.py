from adjacency_list import *

def floyd(distance):
    n = len(distance)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
    return distance


def distance_matrix(adj_lst):
    n = len(adj_lst)
    distance = [[float('inf') for _ in range(n)] for i in range(n)]
    for i in range(n):
        distance[i][i] = 0
        for edge in adj_lst[i]:
            distance[i][edge[0]] = edge[1]
        
    
    return distance

graph_str = """\
D 3 W
0 1 1
1 2 2
2 0 4
"""

adj_list = adjacency_list(graph_str)
dist_matrix = distance_matrix(adj_list)
print("Initial distance matrix:", dist_matrix)
dist_matrix = floyd(dist_matrix)
print("Shortest path distances:", dist_matrix)

import pprint

graph_str = """\
U 7 W
0 1 5
0 2 7
0 3 12
1 2 9
2 3 4
1 4 7
2 4 4
2 5 3
3 5 7
4 5 2
4 6 5
5 6 2
"""

pprint.pprint(floyd(distance_matrix(adjacency_list(graph_str))))