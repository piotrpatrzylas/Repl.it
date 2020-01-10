"""
A flower costs A pounds and B pence. Determine, how many pounds and pence should one pay for N flowers. A program gets three numbers: A, B, N. It should print two numbers: total cost in pounds and pence. 

For exampe, on input 
1
50
3
output should be
4
50
"""
A = int(input())
B = int(input())
N = int(input())
pence = B * N
add_pounds = pence // 100
pounds = (A*N) + add_pounds
pence_left = pence - (add_pounds * 100)
print(pounds)
print(pence_left)
