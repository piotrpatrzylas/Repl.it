"""
Fibonocci numbers are defined as follows:
Zeroth Fibonacci number F(0) is equal 0
Second Fibonacci number F(1) is equal 1
Third Fibonacci number F(2) is equal F(0) + F(1) is equal 1
...
Nth Fibonacci number F(N) is equal F(N-1) + F(N-2)

Given an integer a, determine its index among the Fibonacci numbers, that is, print the number N such that F(N)=a. If a is not a Fibonacci number, print -1. 

For  example on input:
10
output must be
-1
"""
num = int(input())

def fibo(n):
  if n == 1 or n == 0:
    return 1
  return fibo(n-1) + fibo (n-2)
  
def psquare(n):
  out = 5*n**2 + 4
  out2 = 5*n**2 - 4
  return [out, out2]

isFibo = False

checks = psquare(num)  
if (checks[0]**0.5) % 1 == 0 or (checks[1]**0.5) % 1 == 0:
  isFibo = True

ind = 0

if isFibo:
  for n in range(0, num):
    if num == 2:
      ind = 3
      break
    if fibo(n) == num:
      ind = n+1
      break

if isFibo:
  print(ind)
else:
  print("-1")
