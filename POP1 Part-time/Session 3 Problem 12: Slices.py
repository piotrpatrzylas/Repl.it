"""
You are given a string.
In the first line, print all but the last two characters of the string.
In the second line, print all but the first two characters of the string.
In the third line, print all but the first two characters and the last two characters of the string.

If the specified segment is empty, print [EMPTY] in the corresponding string.

For example, on input:
abracadabra
output must be
abracadab
racadabra
racadab
"""
s = input()
if len(s[:-2]) > 0:
  print(s[:-2])
else:
  print("[EMPTY]")
if len(s[2:]) > 0:
  print(s[2:])
else:
  print("[EMPTY]")
s2 = s[2:]
if len(s2[:-2]) > 0:
  print(s2[:-2])
else:
  print("[EMPTY]")
