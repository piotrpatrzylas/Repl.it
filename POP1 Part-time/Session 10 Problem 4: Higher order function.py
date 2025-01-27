"""
Suppose f is a function that takes a character (string of length 1) as an argument and returns a character. Define a higher order function stringify that takes f as an argument and returns another function F such that:

    F takes a string s as an argument
    F returns a string which is equal to f(s[0])f(s[1])...f(s[n])


Use the pattern on the right for your implementation.

Hint: Have a look at the function vectorize in the lecture slides. 

For example, the result of:

def f(x):
    #change lower case to upper
    return chr(ord(x)-32)

F = stringify(f)

print(F("apple"))


must be

APPLE 


The tests work as follows:

def f(x):
    #change lower case to upper
    return chr(ord(x)-32)
F = stringify(f)

#Test1 checks F("apple")=="APPLE"
def f(x):
    #change upper case to lower
    return chr(ord(x)+32)
F = stringify(f)

#Test2 checks F("APPLE")=="apple"
def f(x):
    #change lower case to upper if vowel
    #otherwise leave unchanged
    if x in {'a', 'e', 'i', 'o', 'u'}:
        return chr(ord(x)-32)
    else:
        return x
F = stringify(f)
#Test3 checks F("apple") == "ApplE"
"""
def stringify(f):
  #provide implementation
  def new_function(x):
    new_object = ""
    for i in x:
      new_object += f(i)
    return new_object
  return new_function
