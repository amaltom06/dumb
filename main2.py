from graphics import rectangle,circle
from graphics.threeDgraphics import cuboid,sphere


length=int(input("enter length of rectangle:"))
width=int(input("enter width rectangle:"))
radius=int(input("enter radius of circle:"))
length=int(input("enter length of cuboid:"))
width=int(input("enter width of cuboid:"))
height=int(input("enter height cuboid:"))
radius=int(input("enter radius of sphere:"))

#using rectangle module
print("area of a rectangle = ",rectangle.area(length,width))
print("perimeter of a rectangle = ",rectangle.perimeter(length,width))

#using circle module
print("area of the circle = ",circle.area(radius))
print("perimeter of the circle = ",circle.perimeter(radius))

#using cuboid module
print("surface area of a cuboid = ",cuboid.surface_area(length,width,height))
print("volume of a cuboid= ",cuboid.volume(length,width,height))

#using sphere module
print("surface area of the circle = ",sphere.surface_area(radius))
print("perimeter of the circle = ",sphere.volume(radius))
