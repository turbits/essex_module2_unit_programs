# +===================================================================+
# Author: Trevor Woodman
# Github: https://github.com/turbits
# Repo: https://github.com/turbits/essex_module2_unit_programs
# Project: Module 2 (OOP_PCOM7E)
# Course: Object Oriented Programming (OOP_PCOM7E September 2022)
# School: University of Essex
# Date: September-December, 2022
# +===================================================================+

class Point:
  x = 0.0
  y = 0.0

  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  def __str__(self):
    return "Point({}, {})".format(self.x, self.y)
  
  def reset(self):
    self.x = 0.0
    self.y = 0.0

def main(point):
  x = 0.0
  y = 0.0

  def __init__(self, x, y):
    self.point.x = float(x)
    self.point.y = float(y)
  
  print "\n"
  print "-" * 20
    # print initial point
  print "Initial Point: {}".format(point)
  
  # is Point.x divisible by 2?
  print "=> Branch: Is Point.x divisible by 2?"
  if point.x % 2 == 0:
    # if yes, divide Point.x by 2
    print "=> Yes: Dividing Point.x by 2"
    point.x /= 2.0
    print "Current Point: {}".format(point)
  else:
    # if no, multiply Point.x by 2
    print "=> No: Multiplying Point.x by 2"
    point.x *= 2.0
    print "Current Point: {}".format(point)

  # Floor Point.x
  print "=> Flooring Point.x"
  point.x = int(point.x)
  
  # return Point
  print "Final Point: {}".format(point)
  print "-" * 20
  print "\n"
  return point

if __name__ == "__main__":
  point1 = Point(4, 1.2)
  point2 = Point(3.2, 2.1)
  point3 = Point(1.1, 3.4)
  point4 = Point(22, 4.3)

  main(point1)
  main(point2)
  main(point3)
  main(point4)

