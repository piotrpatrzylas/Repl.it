"""
Implement a function matrix_max_index(M, m, n) that returns a tuple (i,j) where i is the row number and j is the column number of the maximal element of the martix. The arguments of the function are:

     M - the matrix of numbers (represented as usual by a list of lists)
     m - the number of rows in M
     n - the number of columns in M  


If there exist multiple such elements in different rows, print the one with smaller row number. If there multiple such elements occur on the same row, output the smallest column number. 

For example, the result of

M = [[0, 3, 2, 4], [2, 3, 5, 5],  [5, 1, 2, 3]]

print(matrix_max_index(M, 3, 4)==(1,2))

must be
True
"""
def matrix_max_index(M, m, n):
  i = 0
  j = 0
  for row in range(1, m):
    if max(M[i]) < max(M[row]):
      i = row
  j = M[i].index(max(M[i]))
  return (i, j)

  

