"""
 Given two integers A and B. Print all numbers from A to B inclusively, in ascending order, if A < B, or in descending order, if A ≥ B. 

Recommendation. Use for loops.

For example, on input
4
2
output must be
4 3 2
"""
num1 = int(input())
num2 = int(input())
counter = num1
counter2 = num2

if counter < num2:
  while counter <= num2:
    print(counter)
    counter += 1
elif counter > num2:
  while counter >= num2:
    print(counter)
    counter -= 1
elif num1 == num2:
  print(num1)
