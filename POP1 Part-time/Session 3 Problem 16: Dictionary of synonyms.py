"""
You are given a dictionary consisting of word pairs. Every word is a synonym the other word in its pair. All the words in the dictionary are different.

First line of the input specifies how many word pairs will follow. After the dictionary there is one more word given. Find a synonym for this word.

Hint. To solve the problem quickly, use dictionaries.

For example, on input
3
water liquid
fire heat
python java
fire
output must be
heat
"""
count = int(input())
diki = {}
for i in range(0, count):
  pair = input().split()
  diki[pair[0]] = pair[1]

target = input()
print(diki[target])
