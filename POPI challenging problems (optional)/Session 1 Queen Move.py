"""
Consider representation of chess board as in the problem

Session 1 Problem 15: Chess Board

Chess queen moves horizontally, vertically or diagonally to any number of cells. Given two different cells of the chessboard, determine whether a queen can go from the first cell to the second in one move.

The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the first cell, and then the last two - for the second cell. The program should output YES if a queen can go from the first cell to the second in one move, or NO otherwise.

For example, on input
4
2
6
3
output must be
NO
"""

pos1_row = int(input())
pos1_col = int(input())

pos2_row = int(input())
pos2_col = int(input())

if pos1_row == pos2_row:
  print("YES")
elif pos1_col == pos2_col:
  print("YES")
elif pos1_row - pos2_row == pos1_col - pos2_col:
  print("YES")
else:
  print("NO")