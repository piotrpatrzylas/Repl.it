"""
Attempt this problem after you solved the Linked Lists and Stacks problem (Session 11 Problem 2). This is because you can use your implementation of Stack to solve this problem.

Given a string of parentheses of four types, (), [], {} and <>, print True if the parentheses of the string are balanced, otherwise print False. For the examples of balanced/unbalanced strings and the algorithm to solve this problem using Stack, see Session 11 lecture slides.

For example, on input:

([{}<>])

your output must be:
True
"""
i = input()

class Node:
  def __init__(self, init_data):
    self.data = init_data
    self.next = None

class Stack:
  def __init__(self):
    self.top = None    #top stores a Node
  def push(self, x):
    if x in ("(", "[", "{", "<") or self.top == None:
      new_node = Node(x)
      new_node.next = self.top
      self.top = new_node
    else:
      if self.top.data == "(" and x == ")" or self.top.data == "[" and x == "]" \
      or self.top.data == "{" and x == "}" or self.top.data == "<" and x == ">":
        self.top = self.top.next
      else:
        new_node = Node(x)
        new_node.next = self.top
        self.top = new_node
  def is_empty(self):
    return (self.top == None)

S = Stack()
for el in i:
  S.push(el)

print(S.is_empty())


