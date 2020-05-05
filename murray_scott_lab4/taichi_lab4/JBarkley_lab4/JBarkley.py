"""
Josh Barkley
CSE408
Spring2020
Lab 4 : Part D
"""
###############################################################################
print("Begin problem 3-D (Josh Barkley)")
"""
d. Write a program containing a function to output the fibonacci sum up to a user
inputted number.
"""  
###############################################################################

mynumber = int(input("Up too what number?"))
n1, n2 = 0, 1
count = 0
if mynumber <= 0:
   print("Please enter a positive integer")
else:
   print("Fibonacci sequence:")
   while n1 < mynumber:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
