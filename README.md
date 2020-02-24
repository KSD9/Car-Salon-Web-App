# ProjectName: Aston Martin Car Salon Web App
 Django 2.2 + Python 3 

#Live example
- http://uniexample.touchpython.com/index

# To run the app:
- You must have Python 3 and Django 2.2 installed.
- Clone project repository
- Open folder CarSalon_App_project , and run the following commands:
- Important ! Run This Command In Your Teminal Only Once To Initialize The Project Files:
- python3 projectSetup.py
- The Script will create the db / run all migrations / feed the db with initial data. / run the server.
- Initial Admin Credentials are : Username- admin | Pass- ie123456
- After that run the project by using:
- python3 manage.py runserver
- To use the back office of the system , just type /admin in your browser.
 


# Roles: Super User (System Owner),Administrator,Sales Manager,Rent Manager, Not Logged User

# Not Logged User:
- Can see all the cars
- Can see details about a car
- Can send information emails
- Can book test drives for a car

# Super User (System Owner) charectaristics:
- Can see all the users
- Can delete users
- Can see all the Cars
- Can create Cars
- Can update Cars
- Can delete Cars
- Can sell cars

# Administrator charectaristics:
- Can make sell car requests
- Can make rent car requests



# Sales Manager charectaristics:
- Can make sell car requests

# Rent Manager charectaristics:
- Can make rent car requests


