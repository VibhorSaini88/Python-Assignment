# (Q.1)- Create a circle class and initialize it with radius. 
      # Make two methods getArea and getCircumference inside this class.
class Circle:
	def getArea(self,radius):
        	self.area= 3.14*radius**2
	def getCircumference(self,radius):
		self.circumferenc = radius*2*3.14
	def show(self):
		print("Area of circle: ",self.area)
		print("circumference of circle: ",self.circumferenc)	
a = Circle()
a.getArea(5)
a.getCircumference(5)
a.show()




# (Q.2)- Create a Student class and initialize it with name and roll number. Make methods to :
      # 1. Display - It should display all informations of the student.
class student:
	def name(self,name,roll_number):
		self.name = name
		self.roll_number = roll_number
	def display(self):
		print(self.name,self.roll_number)
		
s = student()
s.name("vibhor",88)
s.display()




# (Q.3)- Create a Temprature class. Make two methods :
      # 1. convertFahrenheit - It will take celsius and will print it into Fahrenheit.
      # 2. convertCelsius - It will take Fahrenheit and will convert it into Celsius.
class Temprature:
	def fahrenheit(self,celsias):
		self.fahrenhait  = celsias*1.8+32
	def celsius(self,fahrenhait):
		self.celsias = ((fahrenhait-32)*5)/9
	def display(self):
		print(self.fahrenhait)
		print(self.celsias)
		
obj = Temprature()
obj.fahrenheit(15)
obj.celsius(13)
obj.display()




# (**Q.4)- Create a class MovieDetails and initialize it with Movie name, artistname,Year of release and ratings .
        # Make methods to -->
        # 1. Display-Display the details.
		  # 2. Update- Update the movie details.
class MovieDetails:
		def informations(self,movie_name,artist_name,year_of_release,ratings):
			self.movie_name      = movie_name
			self.artist_name     = artist_name
			self.year_of_release = year_of_release
			self.ratings		 = ratings
		def display(self):
			print("movie name: ",self.movie_name)
			print("artist name: ",self.artist_name)
			print("year_of_release: ",self.year_of_release)
			print("ratings: ",self.ratings)
		def update(self):
			self.movie_name      = input("write movie name: ")
			self.artist_name     = input("write artist name: ")
			self.year_of_release = int(input("write year of release: "))
			self.ratings         = int(input("write ratings: "))
			
cinema = MovieDetails()
cinema.informations("Robot","mukesh kumar",2018,5)
cinema.display()
cinema.update()
cinema.display()




# (Q.5)- Create a class Expenditure and initialize it with expenditure,savings.Make the following methods. 
# 1. Display expenditure and savings. 
# 2. Calculate total salary.
# 3. Display salary.
class Expenditure:
	def salary(self):
		self.Expenditur = int(input("Enter {day or month or year} Expenditure: "))
		self.Savings     = int(input("Enter {day or month or year} Savings: "))
	def display(self):
		print("Expenditure {day or month or year}: ",self.Expenditur)
		print("Savings {day or month or year}: ",self.Savings)
	def calculate(self):
		self.Total_salary = self.Expenditur + self.Savings
	def show(self):
		print("total salary of {day or month or year}:-> ",self.Total_salary)
			
entity = Expenditure()
entity.salary()
entity.display()
entity.calculate()
entity.show()