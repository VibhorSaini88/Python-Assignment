#(Q.1)- Create a class Animal as a base class and define method animal_attribute. Create another class Tiger which is inheriting Animal and access the base class method.
class Animal:
	def animal_attribute(self,name):
		self.name = name
	def show(self):
		print(self.name)
		print("this is an Animal.")
		print( )

class Tiger(Animal):
	def attribute(self,variable):
		self.variable = variable
	def show1(self):
		print(self.variable)
		print("It is the ",self.variable)
being = Tiger()
being.animal_attribute("cow")
being.show()
being.attribute("Tiger")
being.show1()
	
	
	
#(Q.2)- What will be the output of following code.
#Eg:-> 
# class A:
    # def f(self):
        # return self.g()

    # def g(self):
        # return 'A'

# class B(A):
    # def g(self):
        # return 'B'

# a = A()
# b = B()
# print a.f(), b.f()
# print a.g(), b.g()

# modified from Eg:->  
class Apple:
	def fun(self):
		return self.get()
	def get(self):
		return 'A'
class Ball(Apple):
	def get(self):
		return 'B'
a = Apple()
b = Ball()
print (a.fun(),b.fun())
print (a.get(),b.get())

#{Output(solution)}=> A B
#                     A B 



#(Q.3)- Create a class Cop. Initialize its name, age , work experience and designation. Define methods to add, display and update the following details. Create another class Mission which extends the class Cop. Define method add_mission _details. Select an object of Cop and access methods of base class to get information for a particular cop and make it available for mission.
class cop:
	def information(self,name,age,workExperience,designation):
		self.name = name
		self.age  = age
		self.workExperience = workExperience
		self.designation    = designation
	def display(self):
		print( )
		print("cop name: ",self.name)
		print("cop age: ",self.age)
		print("cop Experience: ",self.workExperience)
		print("cop designation: ",self.designation)
	def update(self):
		self.name = input("enter cop name: ")
		self.age  = int(input("enter cop age: "))
		self.workExperience = int(input("enter cop experience: "))
		self.designation    = input("cop designation: ")
class Mission(cop):
	def add_mission(self,mission):
		print("cop mission no.: ",mission)
		print( )
	
pro = cop()	
obj = Mission()
obj.information("mukesh",30,5,"security")
obj.display()
obj.add_mission(1)
obj.update()
obj.display()
obj.add_mission(5)



#(Q.4)- Create a class Shape.Initialize it with length and breadth Create the method Area. Create class rectangle and square which inherits shape and access the method Area.
class shape:
	def area(self,length,breadth):
		self.length  = length
		self.breadth = breadth
class rectangle(shape):
	def area1(self):
		self.areas = self.length*self.breadth
		print("area of a rectangle: ",self.areas)
class square(rectangle):
	def area2(self):
		self.length  = int(input("enter length for square; "))
		self.breadth = int(input("enter same breadth for square: "))
		self.areas = self.length*self.breadth
		print("area of a square: ",self.areas)
		
math = square()
math.area(5,10)
math.area1()
math.area2()
	