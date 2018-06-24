class Mathematics:
	def operation(self,number):
		if number>6:
			print("out of no.")
		else:
			i = int(input("enter any no. "))
			j = int(input("enter any another no. "))
			if number==1:
				print("addition of two no.")
				add = i + j
				print("sum is:- ",add)
			elif number==2:
				print("subtraction of two no.")
				sub = i - j
				print("sum is:- ",sub)
			elif number==3:
				print("multiplicationcation of two no.")
				mul = i * j
				print("sum is:- ",mul)
			elif number==4:
				print("devision of two no.")
				dev = i / j
				print("sum is:- ",dev)
			elif number==5:
				print("power of no.")
				p1 = i**2
				p2 = j**2
				print("sum is:- ",p1)
				print("sum is:- ",p2)
			else:
				import math
				print("factorial of two no's:- ",math.factorial(i))
				print(math.factorial(j))
				
						
number = int(input("enter 1.for addition or 2 for subtraction or 3 for multiplication: "))
obj = Mathematics()
obj.operation(number)