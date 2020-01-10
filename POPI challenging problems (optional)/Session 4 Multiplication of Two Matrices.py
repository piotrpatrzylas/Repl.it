"""
Let

    A be a matrix of the size m x n (m rows, n colums)
    B be a matrix of the size n x r

The result of multiplication A x B is a matrix C of the size m x r such that its element at position (i, k) is equal to following sum:

    A[i][1]∗B[1][k]+⋯+A[i][n]∗B[n][k]


Implement the fruitful function matrix_multiplication(A,B,m,n,r) which returns a matrix that is the result of multiplication A x B.

For example, the result of

A = [[0, 1, 2, 3],  [4, 5, 6, 7],  [8, 9, 10, 11]]

B = [[2, 3], [0, 4], [5, -1], [1, 1]]

C = matrix_multiplication(A, B, 3, 4, 2)

print(C)

must be
[[13, 5], [45, 33], [77, 61]]
"""
def matrix_multiplication(A,B, m, n, r):
  C = []
  for i in range(m):
    C.append([])
    for j in range(r):
      num = 0
      num2 = 0
      for el in range(m):
        for el2 in range(n):
          if el == i:
            num = A[el][el2]*B[el2][j]
            num2 += num
      C[i].append(num2)
  return C
