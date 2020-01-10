"""
The text is given in a single line. For each word of the text count the number of its occurrences before it.
A word is a sequence of non-whitespace characters. Two consecutive words are separated by one or more spaces. (Punctuation marks are a part of a word, by this definition.)

For example, on input:
the block on the block on the block on the floor
output must be
0 0 0 1 1 1 2 2 2 3 0
"""
s = input().split()
counter = 0

for ind in range(0, len(s)):
  for ind2 in range(ind, -1, -1):
    if ind == ind2:
      continue
    if s[ind] == s[ind2]:
      counter += 1
  print(counter, end = " ")
  counter = 0

