import pymysql
username=input("Please enter your SQL server username:")
passw=input("Please enter your SQL server password:")
conn=pymysql.connect(host="localhost",user=username,password=passw)
cursor=conn.cursor()
cursor.execute("CREATE DATABASE PROJECT")
print("Database created!!")
cursor.execute("use PROJECT")
cursor.execute("CREATE TABLE Room(ROOM_ID CHAR(20) PRIMARY KEY,ROOM_TYPE CHAR(25),RENT INT,AC CHAR(1),FRIDGE CHAR(1),No_of_beds int,GEYSER CHAR(1));")
cursor.execute("CREATE TABLE Roles(ROLE_NAME CHAR(10) PRIMARY KEY,ROLE_DESC LONGTEXT);")
cursor.execute("CREATE TABLE Login(LOGIN_ID CHAR(10) PRIMARY KEY,USER_NAME LONGTEXT,PASSWORD CHAR(30),ROLE_NAME CHAR(10));")
cursor.execute("CREATE TABLE User(USER_ID CHAR(10) PRIMARY KEY,ROLE_NAME CHAR(10),USER_NAME CHAR(20),USER_MOBILE INT(10),USER_EMAIL CHAR(25),LOGIN_ID CHAR(10) );")
cursor.execute("CREATE TABLE Customer(Cust_Id char(20) Primary key,Cust_Name char(40),Age_18_Above char(1),Cust_Mobile char(10),Cust_Email char(40),Identification_Document char(1));")
cursor.execute("CREATE TABLE Booking(ROOM_ID CHAR(20),START_DATE CHAR(10),END_DATE CHAR(10),BOOKING_ID CHAR(30) PRIMARY KEY ,CUST_ID CHAR(20));")
cursor.execute("CREATE TABLE Payments(Pay_Id CHAR(10) PRIMARY KEY,CUST_ID CHAR(20),P_DATE DATE,AMOUNT INT,DESCRIPTION LONGTEXT,BOOKING_ID CHAR(30));")
cursor.execute("CREATE TABLE Employee(E_Id CHAR(5) PRIMARY KEY,E_Name CHAR(30),SALARY INT);")
print("Tables created!!")
cursor.execute("ALTER TABLE User ADD FOREIGN KEY (ROLE_NAME) REFERENCES Roles(ROLE_NAME);")
cursor.execute("ALTER TABLE User ADD FOREIGN KEY (LOGIN_ID) REFERENCES Login(LOGIN_ID);")
cursor.execute("ALTER TABLE Booking ADD FOREIGN KEY (Cust_Id) REFERENCES Customer(Cust_Id);")
cursor.execute("ALTER TABLE Payments ADD FOREIGN KEY (Cust_Id) REFERENCES Customer(Cust_Id);")
cursor.execute("ALTER TABLE Payments ADD FOREIGN KEY (BOOKING_ID) REFERENCES Booking(BOOKING_ID);")
print("Foreign keys defined")
cursor.execute("INSERT INTO ROOM VALUES('R001','REGULAR',5000,'Y','N',2,'N');")
cursor.execute("INSERT INTO ROOM VALUES('R002','DELUXE',7000,'Y','Y',3,'N');")
cursor.execute("INSERT INTO ROOM VALUES('R003','SUPER DELUXE',8000,'Y','Y',2,'Y');")
cursor.execute("INSERT INTO ROOM VALUES('R004','REGULAR',5000,'Y','N',1,'Y');")
cursor.execute("INSERT INTO ROOM VALUES('R005','REGULAR',4500,'Y','N',1,'N');")
cursor.execute("INSERT INTO ROLES VALUES('ADMIN','The owner can work upon employee as well as customer related operations')")
cursor.execute("INSERT INTO ROLES VALUES('EMPLOYEE','The employee can only work upon customer related operations');")
cursor.execute("INSERT INTO LOGIN VALUES('L001','Saarthak Maini','Saarthak@123','ADMIN');")
cursor.execute("INSERT INTO LOGIN VALUES('L002','Aryan Maini','Aryan@123','ADMIN');")
cursor.execute("INSERT INTO LOGIN VALUES('L004','Devansh Bhanga','Devansh@123','EMPLOYEE');")
cursor.execute("INSERT INTO User VALUES ('U001','ADMIN','Saarthak Maini',981127897,'SM@gmail.com','L001');")
cursor.execute("INSERT INTO User VALUES ('U002','ADMIN','Aryan Maini',981127897,'AM@gmail.com','L002');")
cursor.execute("INSERT INTO User VALUES ('U004','EMPLOYEE','Devansh Bhanga',981123456,'DB@gmail.com','L004');")
cursor.execute("INSERT INTO CUSTOMER VALUES('C001','Avinash Kumar Jha','N','123456789','AV@GMAIL.COM','N');")
cursor.execute("INSERT INTO CUSTOMER VALUES('C002','Bhavya Mohan','Y','133456789','BM@GMAIL.COM','Y');")
cursor.execute("INSERT INTO CUSTOMER VALUES('C003','Siddharth Jain','N','444446789','SJ@GMAIL.COM','N');")
cursor.execute("INSERT INTO Booking VALUES('R001','2016-03-04','2016-03-10','B001','C001');")
cursor.execute("INSERT INTO Booking VALUES('R002','2016-03-04','2016-03-12','B002','C001');")
cursor.execute("INSERT INTO Booking VALUES('R001','2015-03-04','2015-03-03','B003','C001');")
cursor.execute("INSERT INTO Booking VALUES('R004','2018-07-04','2018-07-06','B004','C003');")
cursor.execute("INSERT INTO Employee VALUES('E001','Ashish Chanchalani',5000);")
cursor.execute("INSERT INTO Employee VALUES('E002','Preeti Arora',4000);")
print("Values inserted....")
conn.commit()
conn.close()