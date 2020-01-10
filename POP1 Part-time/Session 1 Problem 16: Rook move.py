"""
Chess rook moves horizontally or vertically on the chessboard. Given two different cells of the chessboard, determine whether a rook can go from the first cell to the second in one move.

The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the first cell, and then the last two - for the second cell. The program should output YES if a rook can go from the first cell to the second in one move, or NO otherwise.

For example, on input
2
3
5
6
output must be 
NO
"""
first_column = int(input())
first_row = int(input())
second_column = int(input())
second_row = int(input())

if first_column == second_column or first_row == second_row:
  print("YES")
else:
  print("NO")
