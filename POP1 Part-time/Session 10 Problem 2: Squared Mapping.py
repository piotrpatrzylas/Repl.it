"""
 Given lists of integer objects X = [x1, .., xn] and Y = [y1,..., yn], produce an iterator to the sequence (x1*x1, y1), (x2*x2, y2), ... (xn*xn, yn). 
 
Important. Provide an implementation using the pattern on the right and a zip expression. This expression must replace ... and the rest of the pattern must not be edited.

For example, the input:
 
1 2 3
5 6 7

output must be
 
1 5
4 6
9 7
"""
X = [int(x) for x in input().split()]
Y = [int(x) for x in input().split()]

it_squared_mapping = zip([x*x for x in X], Y) #insert a zip expression here

for x in it_squared_mapping: print(x[0], x[1])
