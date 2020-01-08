"""
Consider representation of a chess board as in 

Session 1 Problem 15: Chess Board

Chess knight moves like the letter L. It can move two cells horizontally and one cell vertically, or two cells vertically and one cells horizontally. Given two different cells of the chessboard, determine whether a knight can go from the first cell to the second in one move.

The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the first cell, and then the last two - for the second cell. The program should output YES if a knight can go from the first cell to the second in one move, or NO otherwise.

For example, on input
2
1
1
3
output must be 
YES
"""

pos1_row = int(input())
pos1_col = int(input())

pos2_row = int(input())
pos2_col = int(input())

if abs(pos1_row - pos2_row) == 1 and abs(pos1_col - pos2_col) == 2:
  print("YES")
else:
  print("NO")