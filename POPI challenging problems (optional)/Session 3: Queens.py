"""
Given a placement of 8 queens on the board, determine if there is a pair of queens that can attach each other on the next move. Print the word NO if no queen can attack another, otherwise print YES. The input consists of eight coordinate pairs, one pair per line, with each pair giving the position of a queen on a standard chess board with rows and columns numbered starting at 1. 

For example, on input:
1 7
2 4
3 2
4 8
5 6
6 1
7 3
8 5
output must be 
NO
"""
queen1 = list(map(int, (input().split())))
queen2 = list(map(int, (input().split())))
queen3 = list(map(int, (input().split())))
queen4 = list(map(int, (input().split())))
queen5 = list(map(int, (input().split())))
queen6 = list(map(int, (input().split())))
queen7 = list(map(int, (input().split())))
queen8 = list(map(int, (input().split())))
mlist = [queen1, queen2, queen3, queen4, queen5, queen6, queen7, queen8]
results = "NO"

def canAttack(pair, pair2):
  if pair[0] == pair2[0] or pair[1] == pair2[1] or abs(pair[0]-pair2[0]) == abs(pair[1]-pair2[1]):
    return True
  else:
    return False
  
for el in range(0, len(mlist)):
  for el2 in range(0, len(mlist)):
    if el == el2:
      continue
    if canAttack(mlist[el], mlist[el2]):
      results = "YES"

print(results)
