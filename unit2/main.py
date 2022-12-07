# +===================================================================+
# Author: Trevor Woodman
# Github: https://github.com/turbits
# Repo: https://github.com/turbits/essex_module2_unit_programs
# Project: Module 2 (OOP_PCOM7E)
# Course: Object Oriented Programming (OOP_PCOM7E September 2022)
# School: University of Essex
# Date: September-December, 2022
# +===================================================================+

# ============ UNIT 2: EMPLOYEE-RELATED FUNCTIONALITY PROGRAM ============
# Write a Python program to achieve basic employee-related functionality which includes retaining employee details and allowing an employee to book a day of annual leave.

import sys

class Employee:
  first_name = ""
  last_name = ""
  _employee_id = 0
  annual_leave = 0

  def __init__(self, first_name, last_name, employee_id, annual_leave):
    self.first_name = first_name
    self.last_name = last_name
    self._employee_id = employee_id
    self.annual_leave = annual_leave
  
  def __str__(self):
    return "Employee Details\nFirst Name: {}\nLast Name: {}\nEmployee ID: {}\nAnnual Leave: {}".format(self.first_name, self.last_name, self._employee_id, self.annual_leave)

  def book_leave(self, days):
    if self.annual_leave >= days:
      self.annual_leave -= days
      return True
    else:
      return False

def main():
  running = True
  employees = []
  
  while running:
    print "\n"
    print "Welcome to the Employee Management System"
    print "------------------------------------------"
    print "Please select an option"
    print "1. Create Employee"
    print "2. View Employee Details"
    print "3. Book Annual Leave"
    print "4. View All Employees"
    print "5. Exit"
    print "------------------------------------------"
    option = int(raw_input("Option: "))

    print "\n"
    if option == 1:
      first_name = raw_input("Enter first name: ")
      last_name = raw_input("Enter last name: ")
      employee_id = employees[-1]._employee_id + 1 if len(employees) > 0 else 1
      annual_leave = int(raw_input("Enter annual leave: "))
      employee = Employee(first_name, last_name, employee_id, annual_leave)
      employees.append(employee)
      print "SUCCESS"
      print "Employee with ID {} created successfully".format(employee_id)
      print "\n"
    elif option == 2:
      employee_id = int(raw_input("Enter employee ID: "))
      if employee_id > len(employees):
        print "ERR"
        print "Employee with ID {} does not exist".format(employee_id)
        print "\n"
        continue
      print "\n"
      employee = employees[employee_id - 1]
      print employee
      print "\n"
    elif option == 3:
      employee_id = int(raw_input("Enter employee ID: "))
      employee = employees[employee_id - 1]
      days = int(raw_input("Enter number of days: "))
      _success = employee.book_leave(days)
      if _success:
        print "\n"
        print "SUCCESS"
        print "Annual leave booked successfully"
      else:
        print "\n"
        print "ERR"
        print "Annual leave could not be booked, insufficient leave"
        print "Remaining annual leave: {}".format(employee.annual_leave)
    elif option == 4:
      for employee in employees:
        print "\n"
        print employee
    elif option == 5:
      running = False
  print "Thank you for using the Employee Management System"
  print "Exiting..."
  sys.exit(0)


if __name__ == "__main__":
  main()
