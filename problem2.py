'''
-------------------------------------------------------------------------------
Name:		problem1.py
Purpose:	Evenly distributing pieces of chicken within Mr. Fabroa's class, and then the rest for him.

Author:	Huang.S

Created:	date in 07/12/2020
------------------------------------------------------------------------------
'''

# Input number of students and pieces of chicken
students = float(input("Input the number of students: "))
pieces_of_chicken = float(input("Input the number of pieces of chicken: "))

# Calculations
distributed_chicken = (pieces_of_chicken //students)
extra = (pieces_of_chicken % students)

# Output of pieces of chicken 
print("If there are " + str(students) + " students and " + str(pieces_of_chicken) + " pieces of chicken, there will be " + str(distributed_chicken) + " piece(s) of chicken distributed between the students and " + str(extra) + " piece(s) of chicken left for Mr. Fabroa.")