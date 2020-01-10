"""
Implement a function word_count(s) that, given a string consisting of words separated by spaces, returns how many distinct words it has. 

For example, the result of 
print(word_count("Such a day is a bad day"))
must be
5
"""
def word_count(s):
  res = set(s.split())
  return len(res)
