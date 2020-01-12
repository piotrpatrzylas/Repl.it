"""
Implement a function create_matrix(m,n) that, given two positive integer numbers m and n, returns a matrix with m rows and n columns such that at each position (i,j) of this matrix, we have the number i+j.

Important. Provide an implementation using the pattern on the right and a list comprehension expression. This expression must replace ... and the rest of the pattern must not be edited. 

Examples and tests are below:

#Test1 checks create_matrix(2,3)== [[0, 1, 2], [1, 2, 3]]

#Test2 checks create_matrix(1,5)== [[0, 1, 2, 3, 4]]

#Test3 checks create_matrix(5,1)== [[0], [1], [2], [3], [4]]

#Test4 checks create_matrix(4,6)== [[0, 1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6], [2, 3, 4, 5, 6, 7], [3, 4, 5, 6, 7, 8]]
"""
def create_matrix(m,n):
  return [[col for col in range(row, n+row)] for row in range(m)]


#and

def create_matrix(m,n):
  return [[i+j for j in range(0,n)] for i in range(0,m)]
