"""
 Given two cells of a chessboard. If they are painted in one color, print the word YES, and if in a different color - NO.

The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the first cell, and then the last two - for the second cell.

It is assumed that the cells are numbered from left to right and from bottom to top, i.e., the bottom left cell has column number 1 and row number 1 while the bottom right cell has column number 8 and row number 1.

For example, on input
1
1
2
6
output must be
YES
"""
hor1 = int(input())
ver1 = int(input())
hor2 = int(input())
ver2 = int(input())

hor_diff = abs(hor1-hor2)
ver_diff = abs(ver1-ver2)

if hor_diff == 0 and ver_diff == 0:
  print("YES")
elif hor_diff == 0 and ver_diff % 2 == 0:
    print ("YES")
elif ver_diff == 0 and hor_diff % 2 == 0:
    print ("YES")
elif ver_diff == hor_diff:
  print("YES")
else:
  print("NO")
