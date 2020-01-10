"""
Implement a fruitful function scale_matrix(M, m, n, c) that returns the scaled matrix M (where the number at each position is multiplied by c) and does not modify M.

For example, the result of:

M = [[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34]]

N = scale_matrix(M, 3, 4, 2)

print(M)

print(N)

must be
[[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34]]
[[22, 24, 26, 28], [42, 44, 46, 48], [62, 64, 66, 68]]
"""
def scale_matrix(M, m, n, c):
  from copy import deepcopy
  N = deepcopy(M)
  for row in range(m):
    for col in range(n):
      N[row][col] = c*N[row][col]
  return N
