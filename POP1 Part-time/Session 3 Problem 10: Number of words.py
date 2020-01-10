"""
Implement a function word_count(s) that, given a string consisting of words separated by spaces. Determine how many words it has. 

Hint. To solve the problem, use the method count. 

For example, the result of 
print(word_count("Such a day is a bad day"))
must be
7
"""
def word_count(s):
  z = s.count(" ") + 1
  return z
