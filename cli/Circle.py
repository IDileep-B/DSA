# write a code to calculate area and circumference of a circle
# using a class circle with radius float value(7.5)
from math import pi
class circle:
    def __init__(self,radius):
        self.radius= radius
    def area(self):
        return pi * self.radius *self.radius
    def circumference(self):
        return 2 * self.radius
r= float (input("Enter the radius of the circle"))
c= circle(r)
print("Area of the circle:",c.area())
print("Circumferenceof the circle:",c.circumference())

 