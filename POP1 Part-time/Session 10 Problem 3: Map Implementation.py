"""
There is a standard Python function 

map(function_of_N_arguments, collection1, ..., collectionN)

Refer to the study resources or documentation to learn what this function should do. 

The purpose of this exercise is to provide you own implementation of the simplified version of this function

binary_map(function_of_2_arguments, collection1, collection2)

Important. Provide an implementation using the pattern on the right and a zip expression. This expression must replace ... and the rest of the pattern must not be edited. 

For example, the result of 

def plus(x,y): 

  return x+y

X = (1,2,3)

Y = [10, 20, 30]

it_Z = binary_map(plus, X, Y)

for z in it_Z: print(z)

must be

11
22
33
"""
def binary_map(func_of_2, col1, col2):
  return ((func_of_2(i,j) for i, j in zip(col1,col2)))  #insert expression here

