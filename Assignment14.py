#(Q.1)- Write a Python program to read last n lines of a file.
c = -1
f = open('test.txt','r')
content = f.readlines()
n = int(input("Enter the number of lines: "))
while c >=-n:
    print(content[c],end="")
    c = c - 1
f.close()



#(Q.2)- Write a Python program to count the frequency of words in a file.
with open('test.txt','r') as f:
    count = f.read()
    word = count.split()
    s = set(word)
    for n in s:
        print(n,word.count(n))



#(Q.3)- Write a Python program to copy the contents of a file to another file.
with open('test.txt','r') as f1:
    with open('test1.txt','w') as f2:
        for line in f1:
            f2.write(line)



#(Q.4)- Write a Python program to combine each line from first file with the corresponding line in second file.
with open('test.txt') as f3:
    with open('test1.txt') as f4:
        for line,line1 in zip(f3,f4):
            print(line+line1)


#(Q.5- Write a Python program to write 10 random numbers into a file.
# Read the file and then sort the numbers and then store it to another file.

import random

def Rand(start, end, num):
    res = []
    for j in range(num):
        res.append(random.randint(start, end))
    return res

num = 10
start = 1
end = 10
res = Rand(start, end, num)
f = open('test3.txt', 'w')
for n in res:
    f.write(str(n))
    f.write("\n")
f.close()

f = open('test3.txt', 'r')
l = f.readlines()
f.close()
l.sort()

f = open('test4.txt', 'w')
for n in l:
    f.write(n)
    f.write("\n")
f.close()
