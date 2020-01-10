"""
 Given a string that may or may not contain a letter of interest. Print the index location of the first and last appearance of f. If the letter f occurs only once, then output its index. If the letter f does not occur, then print -1. 

For example, on input
fearful
output must be
0 4
"""
s = input()

count = s.count("f")

if count == 0:
  print(s.find("f"))
elif count == 1:
  print(s.find("f"))
elif count >= 2:
  print(s.find("f"), s.rfind("f"), end = " ")
