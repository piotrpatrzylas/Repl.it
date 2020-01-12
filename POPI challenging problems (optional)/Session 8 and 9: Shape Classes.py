"""
Fill in the following templeate and expand it by a method covers that checks if (the area of) this Rectangle, Square or Circle covers the (area of ) given other Rectangle, Square, or Circle and returns True/False. See the examples below.

Hint. It may be useful to use standard Python function isinstance(object, class_name)  that checks if a given object is an instance of the class with the given class_name.

r1 = Rectangle(16,4,12,8)
r2 = Rectangle(12,4,6,2)
#Test1 checks r1.covers(r2)==False
s1=Square(19,5,4)
#Test2 checks r1.covers(s1)==True
c1 = Circle(14,6,3)
#Test3 checks r1.covers(c1)==False
c2 = Circle(19,4,2)
#Test4 checks r1.covers(c2)==True
#Test5 checks s1.covers(c2)==False
c3 = Circle(5,5,5)
r3 = Rectangle(3,8,2,4)
#Test6 checks c3.covers(r3)==False
s2 = Square(6,4,4)
#Test7 checks c3.covers(s2)==True
c4 = Circle(6,9,3)
#Test8 checks c3.covers(c4)==False
c5=Circle(3,3,1)
#Test9 checks c3.covers(c5)==True 

After this works, you can try to implement in addition a method overlaps that checks if this Rectangle, Square or Circle overlaps (has any area in common) with the given other Rectangle, Square, or Circle and returns True/False. We do not provide examples, test cases, or a model solution for overlaps, please create your own tests to check if your implementation is correct.
"""
class Shape:
  def __init__(self, X, Y):
    self.x = X 
    self.y = Y
  
class Rectangle(Shape):
  def __init__(self, X, Y, SideX, SideY):
    super().__init__(X,Y)
    self.sideX = SideX
    self.sideY = SideY
    
  def covers(self, other):
    if isinstance(other, Rectangle):
      return self.x + self.sideX/2 >  other.x + other.sideX/2 and \
      self.x - self.sideX/2 <  other.x - other.sideX/2 and \
      self.y + self.sideY/2 >  other.y + other.sideY/2 and \
      self.y - self.sideY/2 <  other.y - other.sideY/2
      
    if isinstance(other, Circle):
      return self.x + self.sideX/2 >  other.x + other.radius and \
      self.x - self.sideX/2 <  other.x - other.radius and \
      self.y + self.sideY/2 >  other.y + other.radius and \
      self.y - self.sideY/2 <  other.y - other.radius
      
class Square(Rectangle):
  def __init__(self, X, Y, Side):
    super().__init__(X,Y, Side, Side)
    self.side = Side
    

class Circle(Shape):
  def __init__(self, X, Y, Radius):
    super().__init__(X,Y)
    self.radius = Radius
    
  def covers(self, other):
    if isinstance(other, Rectangle):
      d1 = ((other.x + other.sideX/2 - self.x)**2+(other.y + other.sideY/2 - self.y)**2)**0.5
      d2 = ((other.x + other.sideX/2 - self.x)**2+(other.y - other.sideY/2 - self.y)**2)**0.5
      d3 = ((other.x - other.sideX/2 - self.x)**2+(other.y + other.sideY/2 - self.y)**2)**0.5
      d4 = ((other.x - other.sideX/2 - self.x)**2+(other.y - other.sideY/2 - self.y)**2)**0.5
      return max(d1,d2,d3,d4) <= self.radius
    if isinstance(other, Circle):
      return ((other.x - self.x)**2+(other.y - self.y)**2)**0.5+other.radius <= self.radius
