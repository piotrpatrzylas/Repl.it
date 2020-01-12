"""
A doubly linked list is a modification of a linked lists where each Node, in addition to a reference to the next Node, stores a reference to the previous Node. To understand how to work with doubly linked lists, consider an example below that constructs a list of three nodes

class Node:
    def __init__(self, init_data):
     self.data = init_data
     self.next = None
     self.previous = None

head = Node(4)
new_node = Node(6)
new_node.next = head
head.previous = new_node
head = new_node
new_node = Node(7)
new_node.next = head
head.previous = new_node


and the Python Tutor illustration of how it works https://goo.gl/xdq86W.

Now, use doubly linked lists to implement a Queue (similarly to how we previously used simple linked lists to implement a Stack). Use the pattern on the left for your implementation.

Your implementation must support the following examples/tests:
 
q = Queue()
#Test1 checks q.is_empty()==True
q.enqueue(1)
#Test2 checks q.is_empty()==False
q.enqueue(2)
n = q.dequeue()
#Test3 n==1 
q.enqueue(3)
q.dequeue()
n=q.dequeue()
#Test4 check n==3
#Test5 checks q.is_empty()==True
"""

class Node:
  def __init__(self, init_data):
    self.data = init_data
    self.next = None
    self.previous = None

class Queue:
  def __init__(self):
    self.front = None
    self.back = None
    
  def enqueue(self, x):
    new_node = Node(x)
    new_node.next = self.back
    if self.back != None: self.back.previous = new_node
    self.back = new_node
    if self.front == None:
      self.front = self.back
      
  def dequeue(self):
    n = self.front.data
    self.front = self.front.previous
    return n
  def is_empty(self):
    return self.front == None
