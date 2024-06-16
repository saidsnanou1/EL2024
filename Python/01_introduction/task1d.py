import math as M


def calculate_circle_area(radius):
    area = M.pi * radius * radius
    return area


radius = float(input("Please enter the radius of the circle: "))
area_of_the_circle = calculate_circle_area(radius)
print(f"The area of the circle with radius {radius} is: {area_of_the_circle}")
