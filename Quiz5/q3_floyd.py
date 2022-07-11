from adjacency_list import adjacency_list

def floyd(distance):
    """Takes the distance matrix of a weighted graph object and uses 
    Floyd-Warshall algorithm to compute all-pairs shortest paths"""
    n = len(distance)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
    return distance


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