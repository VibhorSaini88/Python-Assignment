#(Q.1)- Extract the user id, domain name and suffix from the following email addresses.
# emails = "zuck26@facebook.com" ; "page33@google.com" ; "jeff42@amazon.com"
# desired_output = [('zuck26', 'facebook', 'com'), ('page33', 'google', 'com'), ('jeff42', 'amazon', 'com')].
print("Ans.(1)->")

import re
email = "zuck26@facebook.com page33@google.com jeff42@amazon.com"
p = re.compile(r"[A-Za-z0-9A-Za-z][A-za-z0-9A-za-z][A-za-z0-9A-za-z]+")
result = p.findall(email)
print(result)
print( )



#(Q.2)- Retrieve all the words starting with ‘b’ or ‘B’ from the following text.
#text = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butte
print("Ans.(2)->")

text = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butte"
p = re.compile(r"B[A-za-z]+")
result = p.findall(text)
print(result)
result = p.finditer(text)
for r in result:
    print(r)
print()
p = re.compile(r"b[A-za-z]+")
result = p.findall(text)
print(result)
result = p.finditer(text)
for r in result:
    print(r)
print()



#(Q.3)- Split the following irregular sentence into words 
# sentence = "A, very very; irregular_sentence"
# desired_output = "A very very irregular sentence"
print("Ans.(3)->")

text = "A very very irregular_sentence"
p = re.sub(r"_"," ",text)
print(p)
print( )


#               ***Optional Question***
#(Q.4)- Clean up the following tweet so that it contains only the user’s message. That is, remove all URLs, hashtags, mentions, punctuations, RTs and CCs.
#tweet = "Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats"
#desired_output = 'Good advice What I would do differently if I was learning to code today'
print("Ans.(4)->")

tweet = "Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats"
p = re.sub(r"Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats",
           "'Good advice What I would do differently if I was learning to code today'",tweet)
print(p)