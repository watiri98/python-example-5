class Circle:
	def __init__(self,radius):
		self.radius = radius
		

	def area(self):
		radius = self.radius
		area=(3.14)*(radius*radius)
		print(area)

	def circumference(self):
		radius = self.radius
		circumference=2*3.14*(radius)
		print(circumference)
class Square:
	def __init__(self,side):
		self.side = side

	def area(self):
		side = self.side
		area=side*side
		print(area)

	def perimeter(self):
		side = self.side
		P=4*side
		print(P)

class Rectangle:
	def __init__(self,width,length):
		self.width = width
		self.length = length

	def area(self):
		width = self.width
		length = self.length
		A=width*length
		print(A)

	def perimeter(self):
		width = self.width
		length = self.length
		P=2(width+length)
		print(P)

class Sphere:
	def __init__(self,radius):
		self.radius = radius

	def surface_area(self,surface_area):
		surface_area= (4*3.14)*(r*r)
		print(surface_area)

	def volume(self,volume):
		volume = (4/3*3.14)*(r*r*r)
		print(volume)


