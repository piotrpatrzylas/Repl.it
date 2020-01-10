"""
Write a function distance(x1,y1,x2,y2) to compute the distance between the points (x1, y1) and (x2, y2).

Use the well-known formula (recall Pyhagorean theorem).

For computing the square root of a number N you can use the function math.sqrt() from the Python math library imported in the first line of the program. 

Note. It is mandatory to use functions for this exercise. Required function name cannot be changed. 

For example, the output of
d = distance(1,2,6,8)
print(d)  
must be
7.810249675906654
"""
def distance(x1, y1, x2, y2):
  a = abs(x1-x2)
  b = abs(y1-y2)
  return (a**2 + b**2)**0.5
