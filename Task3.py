import math

radius = float(input("Enter radius of the circle: "))
#pow = power, pi = 3.14.....
area = math.pi * math.pow(radius, 2)
print(f"Area: {area:.2f}")
circumference = 2 * math.pi * radius
print(f"Circumference: {circumference:.2f}")
sqrt_area = math.sqrt(area)
print(f"Square root of area: {sqrt_area:.2f}")