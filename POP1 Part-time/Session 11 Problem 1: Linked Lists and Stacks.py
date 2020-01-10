"""
Implement a stack using a link list to store the sequence of its elements (see the lecture notes and slides for definitions and details). 

Use the pattern on the left. 

Your implementation must support the following examples/test cases

s = Stack()

#Test1 checks s.is_empty()==True
s.push(1)
s.push(2)
#Test2 checks s.peek()==2 
s.pop()
#Test3 checks s.peek()==1 
#Test4 checks s.is_empty()==False 
s.pop() 
#Test5 checks s.is_empty()==True
"""
class Node:
  def __init__(self, init_data):
    self.data = init_data
    self.next = None

class Stack:
  def __init__(self):
    self.top = None    #top stores a Node
  def push(self, x):
    #implement this: adds a new Node, makes top point to it,
    #old top is "saved in" the new Node's next
    NewNode = Node(x)
    NewNode.next = self.top
    self.top = NewNode
  def pop(self):
    #implement this: makes top point to the next of the Node pointed to by top
    self.top = self.top.next
  def peek(self):
    #implement this: returns the data of the Node pointed to by top
    return self.top.data
  def is_empty(self):
    #implement this: returns True if there are no Nodes in
    #Stack, otherwise False
    return (self.top == None)

