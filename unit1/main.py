# +===================================================================+
# Author: Trevor Woodman
# Github: https://github.com/turbits
# Repo: https://github.com/turbits/essex_module2_unit_programs
# Project: Module 2 (OOP_PCOM7E)
# Course: Object Oriented Programming (OOP_PCOM7E September 2022)
# School: University of Essex
# Date: September-December, 2022
# +===================================================================+

# ============ UNIT 1: "A PROGRAM THAT INCORPORATES PROTECTED AND UNPROTECTED VARIABLES" ============

# Write a Python program that incorporates protected and unprotected variables.

# TREVOR NOTE: the concept of private or protected variables doesn't exist in python, but the common convention is to prefix a variable with an underscore to indicate that it is protected. In C#, a protected variable is accessible only within its class and derived class instances. Commonly, to modify a protected variable, public getter and setter methods are used, which I'll do here.

class Item:
  _id = 0
  name = 0

  def __init__(self, _id, name):
    self._id = _id
    self.name = name

  def __str__(self):
    return "Item Details\nID: {}\nName: {}".format(self._id, self.name)

  def get_id(self):
    return self._id

  def set_id(self, id):
    self._id = id

def main():
  item = Item(1, "Iron Ore")

  print "\nOn creation, item ID is 1..."
  def print_item_details():
    print item
  print_item_details()

  print "\nSetting item ID to 4 using public setter..."
  item.set_id(4)
  print_item_details()

if __name__ == "__main__":
  main()
