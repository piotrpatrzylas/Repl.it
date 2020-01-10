"""
In this exercise, we will work with a non-fruitful recursive function. Implement such a function print_01_strings(k,s,n) that, given a string s of length k, prints all the length n completions of s by the characters 0 and 1, in alphanumeric order. 

Naturally, when print_01_strings(0,'',n) is called, all the 0/1 strings of length n will be printed.

Use the solution sketch provided.

For example, on input:
2
output must be
00
01
10
11
"""
def print_01_strings(k, s, n):
    if k == n:
        print(s)
    else:
        print_01_strings(k+1, s+"0", n)
        print_01_strings(k+1, s+"1", n)


#do not modify below, only implement the function above
n = int(input())
print_01_strings(0,"",n) 
