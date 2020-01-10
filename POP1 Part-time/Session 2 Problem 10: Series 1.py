"""
Given two integers A and B (A ≤ B). Print all numbers from A to B inclusively. 

Recommendation. Use for loops.

For example, on input
4
7
output must be
4 5 6 7
"""
num1 = int(input())
num2 = int(input())
counter = num1

while counter <= num2:
  print(counter, end = " ")
  counter += 1
  
