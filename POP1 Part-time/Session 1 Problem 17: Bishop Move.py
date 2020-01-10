"""
 In chess, the bishop moves diagonally, any number of squares. Given two different squares of the chessboard, determine whether a bishop can go from the first to the second in one move.

The program receives as input four numbers from 1 to 8, specifying the column and row numbers of the starting square and the column and row numbers of the ending square. The program should output YES if a Bishop can go from the first square to the second in one move, or NO otherwise.

For example, on input
2
3
5
6
output must be
YES
"""
first_column = int(input())
first_row = int(input())
second_column = int(input())
second_row = int(input())

col_diff = abs(first_column - second_column)
row_diff = abs(first_row - second_row)

if col_diff == row_diff:
  print("YES")
else:
  print("NO")
