"""
Implement a function concat(s1, s2) concatenating the string s1 with s2 and adding a space inbetween.

For example, the result of
s = concat("John", "Doe")
print(s)
must be
John Doe
"""
def concat(s1, s2):
  word = s1 + " " + s2
  return word
  
s = concat("John", "Doe")
print(s)
