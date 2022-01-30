"""This program is a calculator that can compute the area of triangles and circles. Program prompts users to select a shape, then it calculates the shape and finally - prints the area of that shape to the user!
"""

print ("Starting the calculator...")

option = input("Enter C for Circle or T for Triangle: ")

if option == 'C':
  radius = float(input("Enter radius: "))
  area = 3.14159 * (radius**2)
  print ("Area: %f" % area)