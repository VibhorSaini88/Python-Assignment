#(Q.1)- Create a database. Create the following tables:
# 1. Book
# 2. Titles
# 3. Publishers
# 4. Zipcodes
# 5. AuthorsTitles
# 6. Authors
# Refer to the diagram below.

import pymysql as py
try:
    db = py.connect("localhost",'root','vibhor','assignment')
    cursor = db.cursor()
    qr = "show databases"
    cursor.execute(qr)
    qr1 = "use assignment"
    cursor.execute(qr1)
    qr2 = "create table Book(book_ID int,Title_ID int,Genre varchar(10),Location varchar(15))"
    cursor.execute(qr2)
    qr3 = "create table Titles(Title_ID int,Title varchar(30),ISBN int,Publisher_ID int,Publication_year int)"
    cursor.execute(qr3)
    qr4 = "create table Authors(Author_ID int,First_Name char(15),Middle_Name varchar(15),Last_Name varchar(15))"
    cursor.execute(qr4)
    qr5 = "create table Authors_Titles(Author_Title_ID int,Author_ID int,Title_ID int)"
    cursor.execute(qr5)
    qr6 = "create table Publishers(Publisher_ID int,Name varchar(15),Street_Address varchar(35),Suit_Number int,Zip_code_ID int)"
    cursor.execute(qr6)
    qr7 = "create table Zip_Codes(Zip_Code_ID int,City varchar(10),State varchar(10),Zip_Code int)"
    cursor.execute(qr7)
    result = cursor.fetchall()
    for r in result:
        print(r)
        db.commit()
except:
    db.rollback()
db.close()


#(Q.2)- Insert values in the tables.

db = py.connect("localhost",'root','vibhor','assignment')
cursor = db.cursor()
qr1 = "insert into Book values(105,1045,'knowledge','Mumbai')"
cursor.execute(qr1)
qr2 = "insert into Titles values(1002,'goodHabits',4325,11885,2018)"
cursor.execute(qr2)
qr3 = "insert into Authors values(102,'Amit','kumar','dev')"
cursor.execute(qr3)
qr4 = "insert into Authors_Titles values(1005,256,1010)"
cursor.execute(qr4)
qr5 = "insert into Publishers values(2211,'Rahul','gitaVihar',3880,544)"
cursor.execute(qr5)
qr6 = "insert into zip_codes values(812,'Mullana','Haryana',1303)"
cursor.execute(qr6)
cursor.fetchall()
db.commit()
db.close()

#(Q.3)- Update any values in any of the tables. Print the original and updated values.

db = py.connect("localhost",'root','vibhor','assignment')
cursor = db.cursor()
qr = "update Book set Title_id =1 where Location='Mumbai'"
cursor.execute(qr)
cursor.fetchall()
db.commit()
db.close()
