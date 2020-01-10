"""
 You are given a string. Delete from it all the characters whose indices are divisible by 3.(Recall that the first element has an index 0)

For example, on input:
abracadabra
output must be:
brcaaba
"""
s = list(input())
ns = "" 
for el in range(0, len(s)):
  if el % 3 != 0:
    ns += str(s[el])

print(ns)
