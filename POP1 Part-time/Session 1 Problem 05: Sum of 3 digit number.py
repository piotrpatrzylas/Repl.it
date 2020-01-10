"""
 Given a three-digit number, find the sum of its digits.

Hint. For an interger number N, its last digit can be found as follows:
last_dig = N % 10
Its second last number can be found as follows:
second_last_dig = (N // 10) % 10

For example, on input 
163
the output should be 
10 
"""
N = int(input())
last_dig = N % 10
second_last_dig = (N // 10) % 10
first_dig = (N//100) % 10
print(first_dig + second_last_dig + last_dig)

