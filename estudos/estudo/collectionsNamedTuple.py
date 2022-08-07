from collections import namedtuple

Point = namedtuple('Point', 'x,y')
pt1 = Point(1,2)
pt2 = Point(3,4)
print(Point, pt1, pt2)
dot_product = (pt1.x * pt2.x) + (pt1.y * pt2.y)
print(dot_product)


Car = namedtuple('Car', 'Price Mileage Colour Class')
xyz = Car(Price=10000, Mileage=30, Colour="Cyan", Class='y')
print(Car, xyz)
print(xyz.Class)
