"""
In this exercise, we will work with circular sectors of circles centred at (0,0). Such sectors will be specified by three numbers:

    the angle (in degrees between 0 and 359) that the segment starts from (fr)
    the angle (in degrees between 0 and 359) that the segment ends (to)
    the radius (rad)

All of the above are integer numbers and the angles are counted from the direction of the positive x axis.

Moreover, you may assume that the from angle is always smaller or equal to the to angle (fr <= to). (If you'd like, after you have a working solution, you can solve a more challenging version of this problem when this simplification is removed.) 

To implement, follow the pattern on the left. The examples of how the class is used and tested are below:

s1 = Sector()
s1.fr = 0
s1.to = 20
s1.rad = 40
#Test1 checks str(s1)=="0 20 40"
s1.rotate(50)
#Test2 checks str(s1)=="50 70 40"
s2 = Sector()
s2.fr = 50
s2.to = 70
s2.rad = 40
#Test3 checks s1==s2
s2.fr = 60
s2.to = 100
s2.rad = 30
s3 = s1.intersect(s2)
#Test4 checks str(s3)=="60 70 30"
"""
class Sector:
  def __init__(self):
    self.fr = 0
    self.to = 0
    self.rad = 0
  def rotate(self, angle):
    #implement this
    #rotates sector by angle
    #you man assume the rotation never results in a sector with fr > to
    #(it is optional to solve this problem without this assumption; see above)
    self.fr += angle
    self.to += angle
    
  def intersect(self, other):
    #implement this
    #returns sector (i.e., object of class Sector) that is intersection
    #of this and other sector
    #you may assume that the two sectors have nonempty intersection
    new_object = Sector()
    new_object.fr = max(self.fr, other.fr)
    new_object.to = min(self.to, other.to)
    new_object.rad = min(self.rad, other.rad)
    return new_object
    
  def is_empty(self):
    #implement this
    #returns True if the sector has empty area, otherwise False
    return self.fr == self.to or self.rad == 0

  def __eq__(self, other):
    #implement this
    #returns True this sector is the same as the other, otherwise False
    return self.fr == other.fr and self.to == other.to and self.rad == other.rad
  
  def __str__(self):
    #implement this
    #returns string "F T R" where F is from angle, T is to, and R is radius
    return str(self.fr)+ " " + str(self.to) + " "+ str(self.rad)
