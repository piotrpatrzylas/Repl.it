"""
First line of the input is a number, which indicates how many pairs of words will follow (each pair in a separate line). The pairs are of the form COUNTRY CITY specifying in which country a city is located. The last line is the name of a city. Print the number of cities that are located in the same country as this city.

Hint. Use dictionaries. 

For example, on input:
6
UK London
US Boston
UK Manchester
UK Leeds
US Dallas
Russia Moscow
Manchester
output must be:
3
"""
counter = int(input())
d = {}
for i in range(0, counter):
  p = input().split()
  d[p[1]] = p[0]
  
target = input()
target = d[target]
counter = 0
for val in d.values():
  if val == target:
    counter += 1
    
print(counter)
