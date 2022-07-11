def fib(n):
    """Computes the nth fibonacci number in log n time"""
    M = [[1, 1],
         [1, 0]]    
    
    if n == 0:
        return 0
    quick_power_matrix(M, n - 1)
    return M[0][0]


def matrix_mult(m1, m2):
    """Dot products two 2x2 matrices"""
    a = m1[0][0] * m2[0][0] + m1[0][1] * m2[1][0]
    b = m1[0][0] * m2[1][0] + m1[0][1] * m2[1][1]
    c = m1[1][0] * m2[0][0] + m1[1][1] * m2[1][0]
    d = m1[1][0] * m2[1][0] + m1[1][1] * m2[1][1]
    
    m1[0][0] = a
    m1[0][1] = b
    m1[1][0] = c
    m1[1][1] = d
    

def quick_power_matrix(matrix, n):
    """Peforms fast exponentiation on a matrix"""
    # ---start student section---
    M = [[1, 1],
              [1, 0]]
    
    if n == 0 or n ==1:
        return
    
    quick_power_matrix(matrix, n//2)
    matrix_mult(matrix, matrix)
    
    if n%2 != 0:
        matrix_mult(matrix, M)

print(fib(5))
print(fib(6))
print(fib(7))
print(fib(100))       