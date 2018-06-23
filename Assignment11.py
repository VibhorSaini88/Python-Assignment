#(Q.1)- Create a threading process such that it sleeps for 5 seconds and then prints out a message.
import threading
from threading import Thread
import time

def show():
	print("wait for 5 seconds.")
	time.sleep(5)
	print("Hello python",threading.current_thread())
	
t=Thread(target=show)
t.setName("First")
t.start()


#(Q.2)- Make a thread that prints numbers from 1-10, waits for 1 sec between.
def numbers():
	t  = threading.current_thread()
	print("wait for 1 sec:")
	for x in range(1,10):
		print("sr.no.= ",x,t,id)
		time.sleep(1)
		
t1=Thread(target=numbers,args=())
t1.start()


#(Q.3)- Make a list that has 5 elements.Create a threading process that prints the 5 elements of the list with a delay of multiple of 2 sec between each display.
# Delay goes like 2sec-4sec-6sec-8sec-10sec.
def list():
	l = [2,4,6,8,0]
	t = threading.current_thread()
	for x in l:
		time.sleep(2)
		print("list no. ",x,t)
		
t2=Thread(target=list)
t2.setName("first")
t2.start()

# (Q.4)- Call factorial function using thread.
import math
def factorial():
	t = threading.current_thread()
	id = t.ident
	n = 4
	time.sleep(1)
	print("factorial of 4 is: ",math.factorial(n),t,id)

t3 = Thread(target=factorial)
t3.setName("second")
t3.start()


	
