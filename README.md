# Hotel Management Project

## <strong>Description</strong>

This is a Hotel Management Project.

<strong>My Thinking</strong>

I am at a hotel , in that hotel I have a reception, and at the reception there is a computer. Now, in this computer I am maintaining a database where I am storing the records of all my customers, all my employees, etc. I am also providing a Role Based User Access feature which determines which person can perform which tasks.

For example, the person with the Employee permissions can only change data for the customer table to make bookings , generate bills, etc. On the other hand, the admin or the owner has the permissions to update the employee tables such as incrementing their salaries, adding an employee, etc.

For running the code sample on your laptop/PC, please read the following for setup and installation requirements!

## Note: I have made a video on the same for further reference. I have explained the installation, given a brief about my code sample and showed how to run the program!
<a href="https://youtu.be/GB4nHmv9asA">Link To The Video</a>

We would be downloading:<br>
**Python<br>
SQL<br>
Pymysql module<br>**

**Note: I won't be showing how to download and setup python.**
### Downloading and Installing `Pymysql module`
* Open a new python shell, click on file and then click on Save As.. Option
 ![image](https://user-images.githubusercontent.com/94912101/160825747-f526104d-e8d5-4546-9884-1f2f9ec8470c.png)

* Once you click on the Save As.. Option , file explorer will open! Select the path at the top of the file explorer
* Copy the path(Ctrl + c) <br> ![image](https://user-images.githubusercontent.com/94912101/161272856-0315ce65-419f-4128-a94c-31a6a25d84b8.png)
* Open Command prompt! 
* Enter cd + copied path(ctrl + v) in the terminal
* After that enter cd Scripts
![image](https://user-images.githubusercontent.com/94912101/161273293-4ca94b7b-4036-496c-98fa-a379de593013.png)
* Now type "pip install pymysql" in the command line( We are using the pip package manager to download pymysql from the internet)
* After that press Enter and pymysql package would be downloaded!
![image](https://user-images.githubusercontent.com/94912101/161273718-c2929e0c-d09f-4c99-8dc5-afdf6d5b03e4.png)

### Downloading and Installing `MySQL`
* Go to <a href="https://dev.mysql.com/downloads/installer/">MySQL Download Website</a>
* We would be downloading the community version
![image](https://user-images.githubusercontent.com/94912101/160829622-da0d1751-3ac2-4422-b8ca-405c897fe8c0.png)
* Click on "No thanks, start my download"
<br>
![image](https://user-images.githubusercontent.com/94912101/160830251-dfd4a978-c898-4a24-8414-9fe2d0851a94.png)
* After the installer opens, click on the "Developer Default Option"
![image](https://user-images.githubusercontent.com/94912101/160832206-7578342c-30c2-4ece-93f4-ad0549333b0f.png)
* Now specify your Install directory<br>
![image](https://user-images.githubusercontent.com/94912101/160832796-710943f7-3f36-4f03-9ef7-052d04c61626.png)
* Now a button will come up as "Execute", click it! Installation of the required packages will start!
![image](https://user-images.githubusercontent.com/94912101/160833458-96d38ccd-59c9-43e8-9877-810e717e01b6.png)
* After the installation is complete, click next until you get to the page below
* <b>This is a very important step. By default your username is kept as "root". You would also have to provide a password at this step for the set up. Please remember the Username and Password you are entering as it would be asked while running the program</b>
![image](https://user-images.githubusercontent.com/94912101/160834134-01dcbf0e-bb14-4491-ae04-68843b61d6f4.png)
* Now keep clicking "Next" and "Execute" and the installation would be done!

### Using MySQL shell to look at the database created at the backend(This is optional/Not needed) 
* Go to start and search MySQL shell<br>
 ![image](https://user-images.githubusercontent.com/94912101/160835376-4fb52293-6b73-4f03-8928-c968554b30fd.png)

* After opening it , it would be displayed as given below<br>
![image](https://user-images.githubusercontent.com/94912101/160835699-0bb7ecf0-f72e-4e61-9afc-6c74b6801949.png)

Type the following in the Shell:
\sql
\connect root@localhost
Enter your password: "The password you entered during the set up"
![image](https://user-images.githubusercontent.com/94912101/160836614-22099eca-01c0-4f69-bf5e-f4a4fa36f21e.png)
<br>
You can now use MySQL Shell to check out the tables created for the project

# How to run the code
* The first step is to open your IDE and open the 2 python files given in the repostitory which you can get on you local system by Cloning the repository
* The first file is to create a database on which we would be working on
* Just run the "Project Database" python file and a database would be created with sample data for the hotel management system
![image](https://user-images.githubusercontent.com/94912101/160847883-443716ae-cfd4-4a9c-b062-f7a7e91a5af2.png)

* When you run the program , you would have to provide your SQL username and password(Note: If you didn't specify a user name then it is "root" by default), please do so!<br>
![image](https://user-images.githubusercontent.com/94912101/160848762-18e2de96-46fb-4ea2-9dc1-163a1ca06c79.png)
* Now that our database is created, we can use the other python file for managing the hotel management system database
* Run the other file and you would get a screen asking for your SQL Username and Password. After you fill it you would get the following screen!
![image](https://user-images.githubusercontent.com/94912101/160849780-ecf25299-ddb3-4852-ac09-6249f953d4b4.png)
### The following are the usernames and passwords which you could use to login as an administrator or an employee:
1. Username: Saarthak Maini  Password:Saarthak@123 Role: ADMIN/OWNER
2. Username: Devansh Bhanga Password:Devansh@123 Role:EMPLOYEE

After that you can perform the desired operations as given in the menu




