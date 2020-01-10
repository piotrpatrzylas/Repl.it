"""
Implement the non-fruitful function swap_columns(M, m, n, i, j) that modifies the given matrix M, with m rows and n colums, by swapping the (whole) colums i and j.  

For example, result of 

M =  [[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34]]

swap_columns(M, 3, 4, 0, 1)

print(M)

must be
[[12, 11, 13, 14],  [22, 21, 23, 24], [32, 31, 33, 34]] 
"""
def swap_columns(M, m, n, i, j):
  if i != j:
    for row in range(m):
      for col in range(n):
        if col == i:
          tmp = M[row][col]
          M[row][col] = M[row][j]
          M[row][j] = tmp
