"""
Given a string. Replace every occurrence of the letter f by the letter F, except for the first and the last ones. 

For example, on input:
fifty five
output must be:
fiFty five
"""
string = input()
new_string = ""
for char in range(0, len(string)):
  if char == 0 or char == len(string)-1:
    new_string += string[char]
  elif string[char] == "f":
    new_string += "F"
  else:
    new_string += string[char]
print (new_string)
