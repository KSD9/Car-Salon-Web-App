#!/usr/bin/python3
import sqlite3
import filecmp
import os

os.system("python3 manage.py makemigrations")
os.system("python3 manage.py migrate")

db = "./db.sqlite3"

try:
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute("INSERT INTO\
    auth_user\
    VALUES\
    (Null,'pbkdf2_sha256$100000$ORGPCsmrAH6p$avdyllo367u5PGw7V8wTrhpbUba44lmkiexbYUxLC+w=',Null,1,'admin','John','admin@sample.mail','1','1','2018-07-25 08:46:04.917699','Doe')")

    #Seed Car 1

    cur.execute("INSERT INTO\
    CarSalon_App_carastmar\
    VALUES\
    (Null,'DB9 GT','2017',\'grey','400000','5','450','V8 Diesel','445','4',\
    'The Aston Martin DB9 GT is the most elegant expression of a sports grand tourer, its DNA echoing the iconic DB GT models of its lineage.',\
    'http://hanabi.autoweek.com/sites/default/files/styles/gen-932-524/public/bond-1.jpg?itok=LiCqGWp5')")

    #Seed Car 2 
    cur.execute("INSERT INTO\
    CarSalon_App_carastmar\
    VALUES\
    (Null,'DB 11','2018','black','480000','3','550','V8 Diesel','545','3',\
    'Standard-bearer for an all-new generation of cars, DB11 is the most powerful and efficient ‘DB’production model in Aston Martin’s history. Available as a Coupe with the 5.2-litre twin-turbocharged V12 or the 4.0-litre twin-turbocharged V8 engine, DB11 takes our grand touring heritage to unprecedented heights. ',\
    'https://www.dubaicars.com/uploads/newcars/1818_a0f5dcfad7b393c742355ef436cef603.jpg')")
   

    #Seed Car 3
    cur.execute("INSERT INTO\
    CarSalon_App_carastmar\
    VALUES\
    (Null,'DBS Volante','2018','grey','650000','2','650','V12 Petrolium','645','3',\
    'Some cars like to shout for attention but the DBS Volante has an effortless charisma. It is always centre stage but never overbearing and exudes the unique Aston Martin elegance. The Volante has an understated, timeless movie star quality.',\
    'http://cdn.luxuo.com/2009/07/dbsvolante-1.jpg')")

    #Seed Car 4
    cur.execute("INSERT INTO\
    CarSalon_App_carastmar\
    VALUES\
    (Null,'Vanquish S','2016','black','300000','8','490','V8 Diesel','345','6',\
    'Building on the heritage and success of our flagship Grand Tourer comes the Aston Martin Vanquish S – bringing improved engine power, enhanced dynamics and all new styling to create a car of unprecedented ability. Vanquish S is the ultimate Super GT. ',\
    'https://ag-spots-2017.o.auroraobjects.eu/2017/07/28/other/2880-1800-crop-aston-martin-vanquish-s-volante-2017-c549128072017174833_1.jpg')")
    #Seed Car 5

    cur.execute("INSERT INTO\
    CarSalon_App_carastmar\
    VALUES\
    (Null,'Vanquish Zagato','2017','grey','400000','5','450','V8 Diesel','445','4',\
    'The Vanquish Zagato Concept was unveiled to great acclaim at the prestigious Concorso Eleganza Villa Este at Lake Como, Italy in May 2016. Thanks to unprecedented customer interest, a strictly limited production run of 99 cars will be built to order at Aston Martin production facility in Gaydon, England',\
    'https://www.conceptcarz.com/images/Aston%20Martin/Aston-Vanquish-Zagato-Volante-01-800.jpg')")
 
    #Seed Car 6
    cur.execute("INSERT INTO\
    CarSalon_App_carastmar\
    VALUES\
    (Null,'Vulcan','2017',\'black','400000','5','450','V8 Diesel','445','4',\
    'Introducing the Aston Martin Vulcan – a track-only supercar and our most intense and exhilarating creation to date.',\
    'https://stmed.net/sites/default/files/aston-martin-vulcan-wallpapers-31820-3487015.jpg')")

    conn.commit()
    conn.close()
    print("Data Base Is Seeded")


except Exception as err:
    print(err)

os.system("python3 manage.py runserver")
