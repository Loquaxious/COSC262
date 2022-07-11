"""A program to read a grid of weights from a file and compute the 
   minimum cost of a path from the top row to the bottom row
   with the constraint that each step in the path must be directly
   or diagonally downwards. 
   This question has a large(ish) 200 x 200 grid and you are required
   to use a bottom-up DP approach to solve it.
"""
INFINITY = float('inf')  

def read_grid(filename):
    """Read from the given file an n x m grid of integer weights.
       The file must consist of n lines of m space-separated integers.
       n and m are inferred from the file contents.
       Returns the grid as an n element list of m element lists.
       THIS FUNCTION DOES NOT HAVE BUGS.
    """
    with open(filename) as infile:
        lines = infile.read().splitlines()

    grid = [[int(bit) for bit in line.split()] for line in lines]
    return grid


def grid_cost(grid):
    """The cheapest cost from row 1 to row n (1-origin) in the given grid of
       integer weights.
    """
    n_rows = len(grid)
    n_cols = len(grid[0])
    
    table = [n_cols * [0] for row in range(n_rows)]
    
    for i in range(n_rows):
        for j in range(n_cols):
            if i == 0:
                table[i][j] = grid[i][j]
            else:
                table[i][j] = grid[i][j] + next_min(table, i, j)
    
    best = min(table[n_rows -1])
    return best
    

def next_min(table, i, j):
    """returns the next min value"""
    results = []
    
    for k in range(j-1, j+2):
        try:
            results.append(table[i-1][k])
        except IndexError:
            continue
        
    return min(results)

    
def file_cost(filename):
    """The cheapest cost from row 1 to row n (1-origin) in the grid of integer
       weights read from the given file
    """
    return grid_cost(read_grid(filename))

def print_table(table):
    """Pretty(ish) print of table, row by row"""
    n_rows = len(table)
    n_cols = len(table[0])
    for i in range(n_rows):
        print(f"{i}:",end='')
        for j in range(n_cols):
            print(f"{table[i][j]:5}", end='')
        print()


print(file_cost('medium.txt'))