class circle():
    def __init__(self,radius):
       self.radius=radius
    def area(self):
        return self.pi*(self.radius**2)
r=int(input("Enter radius of circle: "))
obj=circle(r)
print("Area of cicle:",obj.area())

#print()
