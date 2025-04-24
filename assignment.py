#!python3

import sqlite3

import tkinter as tk
from tkinter import *
from tkinter import ttk

"""Assignment: Create a database for a veterinarian. You will need to create your own tables and choose the variable types that best suit these fields/columns. 
There will be 3 tables: 
customers id : primary key integer 
fname: first name 
lname: last name 
phone: phone number 
email: email address 
address: physical address 
city: city where they live 
postalcode: their postal code

pets id: primary key integer 
name: pet name type: dog or cat 
breed: description of breed (example German Sheperd, Mixed, Persion) 
birthdate: birthdate of pet (could be used to calculate their age) 
ownerID: to match the ID number in customers ID

visits id: primary key integer 
ownerid: the id of the owner who brought in their pet. Matches primary key of owner table 
petid: the id of the pet that was brought in. Matches primary key of pets table 
details: details what the visit was about. Could be quite lengthy! 
cost: how much was the visit 
paid: how much has been paid so far, used to find outstanding debts

Create a program that allows you to interface with this database. We will be doing this in parts over the next few classes.

Part 1. Create a function that will add a new customer.
Ask the user for their relevant details and add them to the customers table Optional enhancements. Ideas for Check for duplicates:

Check to see if there is already a username with the same phone number or email before adding and warn that the customer already exists
List all users with the same last name and ask for confirmation before adding
Create a function that will allow you to search for a customer by any part of their record. Example: search for all customers with a specific last name Optional Enhancements.

search for all users that partially match a specific last name
search for multiple criteria"""


file = 'dbase.db'
connection = sqlite3.connect(file)
#print(connection)

cursor = connection.cursor()


qCustomerInfoCreation = """
create table if not exists vetcustomersinfo (
    fname tinytext,
    lname tinytext,
    phone tinytext,
    email tinytext,
    address tinytext,
    city tinytext,
    pCode tinytext);
"""
cursor.execute(qCustomerInfoCreation)
r1 = cursor.fetchall()

qPetInfoCreation = """
create table if not exists petInfo (
    id integer primary key autoincrement,
    petName tinytext,
    type tinytext,
    breed tinytext,
    birthdate date,
    ownerID tinytext);
"""
cursor.execute(qPetInfoCreation)
r2 = cursor.fetchall()

qVisitsCreation = """
create table if not exists visits (
    id integer primary key autoincrement,
    ownerID tinytext,
    petID tinytext,
    details text,
    cost tinyint,
    paid tinyint);
"""
cursor.execute(qVisitsCreation)
r3 = cursor.fetchall()


###Testing to see if I can add a customer

listOfEmail = []
listOfPhone = []

window = tk.Tk()
window.minsize(800,600)



class ChangeCustomer():
    def __init__(self,window):
        self.window = window
        title.destroy()
        Add.destroy()
        Change.destroy()
        Search.destroy()
        tk.Label(window,text="Please enter in all information. \nEnsure that there are no spaces.",font= ('Helvetica',20,'bold')).grid(row=1,column=1,columnspan=4)
        for i in range(7):
            labels[i].grid(column=2,row=(i+2))
            entries[i].grid(column=3,row=(i+2))
        Check.grid(row=9,column=2,columnspan=2)

class SearchCustomer():
    def __init__(self,window):
        self.window = window
        title.destroy()
        Add.destroy()
        Change.destroy()
        Search.destroy()
        tk.Label(window,text="Please enter in the information\nthat you would like to search by. \nEnsure that only one cell is filled.",font= ('Helvetica',20,'bold')).grid(row=1,column=1,columnspan=4)
        for i in range(7):
            labels[i].grid(column=2,row=(i+2))
            entries[i].grid(column=3,row=(i+2))
        Check.grid(row=9,column=2,columnspan=2)

class AddInterface():
    def __init__(self,window):
        self.window = window
        title.destroy()
        Add.destroy()
        Change.destroy()
        Search.destroy()
        tk.Label(window,text="Please enter in all information. \nEnsure that there are no spaces.",font= ('Helvetica',20,'bold')).grid(row=1,column=1,columnspan=4)
        for i in range(7):
            labels[i].grid(column=2,row=(i+2))
            entries[i].grid(column=3,row=(i+2))
        Check.grid(row=9,column=2,columnspan=2)
'''
    try: #Ensure that only email matches one custonmer
        for i in listOfEmail:
            assert email != i
        listOfEmail.append(email)
    except:
        print("Email already linked to a customer.\n Would you like to replace demographics?") 
    try: #Ensure that only one phone number matches one customer
        assert int(phone)
        for i in listOfPhone:
            assert email != i
        listOfPhone.append(phone)
    except:
        listOfEmail.remove(email)
        print("\nCurrent phone number already in use.\nPlease use another phone number.")
        
    print(f'\n\nPlease check your info,\n\n  First Name: {fname}\n  Last Name: {lname}\n  Phone Number: {phone}\n  Email: {email}\n  Address: {address}\n  City: {city}\n  Postal Code: {pCode}')
    check = input('\nAnswer "Yes" if all of the info is correct,\nAnswer "No" if some info is incorrect: ')
    if check=='Yes':
        cursor.execute(f"insert into vetcustomersinfo (fname,lname,phone,email,address,city,pCode) values ('{fname}','{lname}','{phone}','{email}','{address}','{city}','{pCode}');")
        print('Input Complete\n')
    else:
        listOfEmail.remove(email)
        listOfPhone.remove(phone)
        print('Please reenter all of your info.')'''

class addInfo():
    def __init__(self,window):
        self.window = window
        for i in entriesDict:
            



fnlabel = tk.Label(window,text="First Name:")
lnlabel = tk.Label(window,text="Last Name:")
pnlabel = tk.Label(window,text = 'Phone Number:')
elabel = tk.Label(window,text = 'Email Address:')
alabel = tk.Label(window,text = 'Address:')
clabel = tk.Label(window,text = 'City:')
pClabel = tk.Label(window,text = 'Postal Code:')
fname = tk.Entry(window)
lname = tk.Entry(window)
phone = tk.Entry(window)
email = tk.Entry(window)
address = tk.Entry(window)
city = tk.Entry(window)
pCode = tk.Entry(window)
labels = (fnlabel,lnlabel,pnlabel,elabel,alabel,clabel,pClabel)
entries = (fname,lname,phone,email,address,city,pCode) 
entriesDict = {'fname':'','lname':'','phone':'','email':'','address':'','city':'','pCode':''}

title = tk.Label(window,text = "Delta Vet Company!", font= ('Helvetica',40,'bold'), width=20, height=3, borderwidth=5, highlightthickness=2)

Add = tk.Button(window,text = "Add New Customer!", width=18, height=3, borderwidth=5, highlightthickness=2)
Add.config(font=('bold',20),highlightcolor= "black" ,highlightbackground= "black",command=lambda: AddInterface(window))

Change = tk.Button(window,text = "Change Customer Info!", width=18, height=3, borderwidth=5, highlightthickness=2)
Change.config(font=('bold',20),highlightcolor= "black" , highlightbackground= "black")

Search = tk.Button(window,text = "Search Customer Info!", width=18, height=3, borderwidth=5, highlightthickness=2)
Search.config(font=('bold',20),highlightcolor= "black" , highlightbackground= "black",command=lambda: SearchCustomer(window))

Check = tk.Button(window,text = "Done Inputting?", width=18, height=3, borderwidth=5, highlightthickness=2)
Check.config(font=('bold',20),highlightcolor= "black" , highlightbackground= "black",command=lambda: addInfo(window))


title.place(x=90,y=30)
Add.place(x=60,y=200)
Change.place(x=400,y=200)
Search.place(x=250,y=350)


window.mainloop()