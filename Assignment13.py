#(Q.1)- Name and handle the exception occured in the following program:
#a=3
#if a<4:
# a=a/(a-3)
# print(a)

try:
    a = 3
    if a<4:
        a = a/(a-3)
        print(a)
except Exception as e:
    print("Exception Occur")
    print(a)
    print(e)



#(Q.2)- Name and handle the exception occurred in the following program:
#l=[1,2,3]
#print(l[3])

l = [1,2,3]
try:
    print(l[3])
except Exception as index:
    print(index)


#(Q.3)- What will be the output of the following code:
# Program to depict Raising Exception
# try:
#     raise NameError("Hi there")  # Raise Error
# except NameError:
#     print "An exception"
#     raise  # To determine whether the exception was raised or not

try:
    raise NameError("Hi there")
except NameError as message:
    print(message)
    print("An exception")

# OUTPUT=  Hi there
#          An exception

#(Q.4)- What will be the output of the following code:
 # Function which returns a/b
# def AbyB(a , b):
# 	try:
# 		c = ((a+b) / (a-b))
# 	except ZeroDivisionError:
# 		print "a/b result in 0"
# 	else:
# 		print c
# Driver program to test above function
# AbyB(2.0, 3.0)
# AbyB(3.0, 3.0)

def AbyB(a,b):
    try:
        c = (a+b)/(a-b)
    except ZeroDivisionError as e:
        print(e)
        print("a/b result in 0")
    else:
        print(c)

AbyB(2.0,3.0)
AbyB(3.0,3.0)

#OUTPUT= -5.0
#        float division by zero
#        a/b result in 0




#(Q.5)- Write a program to show and handle following exceptions:
# 1. Import Error
# 2. Value Error
# 3. Index Error

try:
    import abcd
except ImportError as e:
    print(e)
try:
    a = 4
    b = 'v'
    c = a+b
    print(c)
except Exception as f:
    print(f)
try:
    l = [2,4,7]
    print(l[4])
except IndexError as g:
    print(g)


#(Q.6)- Create a user-defined exception AgeTooSmallError() that warns the user when they have entered age less than 18.
# The code must keep taking input till the user enters the appropriate age number(less than 18).
class AgeTooSmallError(Exception):
    pass
try:
    i = int(input("Enter any age: "))
    if i < 18:
        raise AgeTooSmallError("This value is too small from 18")
except AgeTooSmallError as e:
        print(e)
else:
    print("this value is too large from 18")
