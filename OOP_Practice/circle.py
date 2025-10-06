import math 
class circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        circle_area = (math.pi) * (self.radius * self.radius)
        return f"area of circle with {self.radius} is {circle_area}"
    
    def circumference(self):
        perimeter = 2 * (math.pi) * self.radius
        return f"Perimeter of circle with {self.radius} is {perimeter}"
    
c = circle(radius = float(input("Enter the radius of circle: ")))
print(c.area())
print(c.circumference())