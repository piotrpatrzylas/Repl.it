"""
 Chess king moves horizontally, vertically or diagonally to any adjacent cell. Given two different cells of the chessboard, determine whether a king can go from the first cell to the second in one move.

The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the first cell, and then the last two - for the second cell. The program should output YES if a king can go from the first cell to the second in one move, or NO otherwise.

For example, on input
2
3
1
4
output should be 
YES
"""
first_column = int(input())
first_row = int(input())
second_column = int(input())
second_row = int(input())

col_diff = abs(first_column - second_column)
row_diff = abs(first_row - second_row)

if col_diff <= 1 and row_diff <= 1:
  print("YES")
else:
  print("NO")
