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


listOfEmail = []
listOfPhone = []


class WindowInterface:
    def __init__(self,window): #defining everything
        self.window = window
        
        self.title = tk.Label(window,text = "Delta Vet Company!", font= ('Helvetica',40,'bold'), width=20, height=3, borderwidth=5, highlightthickness=2)
        self.Add = tk.Button(window,text = "Add New Customer!", width=18, height=3, borderwidth=5, highlightthickness=2,font=('bold',20),highlightcolor= "black" ,highlightbackground= "black",command=lambda:self.AddCustomerInterface(window))
        self.Change = tk.Button(window,text = "Change Customer Info!", width=18, height=3, borderwidth=5, highlightthickness=2,font=('bold',20),highlightcolor= "black" , highlightbackground= "black",command=lambda:self.ChangeCustomerInterface(window))
        self.Search = tk.Button(window,text = "Search Customer Info!", width=18, height=3, borderwidth=5, highlightthickness=2,font=('bold',20),highlightcolor= "black" , highlightbackground= "black",command=lambda: self.SearchCustomerInterface(window))

        self.fnlabel = tk.Label(window,text="First Name:")
        self.lnlabel = tk.Label(window,text="Last Name:")
        self.pnlabel = tk.Label(window,text = 'Phone Number:')
        self.elabel = tk.Label(window,text = 'Email Address:')
        self.alabel = tk.Label(window,text = 'Address:')
        self.clabel = tk.Label(window,text = 'City:')
        self.pClabel = tk.Label(window,text = 'Postal Code:')

        self.fname = tk.Entry(window)
        self.lname = tk.Entry(window)
        self.phone = tk.Entry(window)
        self.email = tk.Entry(window)
        self.address = tk.Entry(window)
        self.city = tk.Entry(window)
        self.pCode = tk.Entry(window)

        self.labels = (self.fnlabel,self.lnlabel,self.pnlabel,self.elabel,self.alabel,self.clabel,self.pClabel)
        self.entries = (self.fname,self.lname,self.phone,self.email,self.address,self.city,self.pCode)
        self.entriesDict = [['fname',''],['lname',''],['phone',''],['email',''],['address',''],['city',''],['pCode','']]
        
        self.AddLabel = tk.Label(window,text="Please enter in all information. \nEnsure that there are no spaces.",font= ('Helvetica',20,'bold'))
        self.SearchLabel = tk.Label(window,text="Please enter in all information\nthat you would like to search by.\nEnsure that there are no spaces.",font= ('Helvetica',20,'bold'))
        self.ChangeLabel = tk.Label(window,text="Please enter in all information. \nEnsure that there are no spaces.",font= ('Helvetica',20,'bold'))

        self.AddButton = tk.Button(window,text = "Done Inputting?", width=18, height=3, borderwidth=5, highlightthickness=2,font=('bold',20),highlightcolor= "black" , highlightbackground= "black",command=lambda: self.AddToDatabase(window))
        self.SearchButton = tk.Button(window,text = "Ready to Search?", width=18, height=3, borderwidth=5, highlightthickness=2,font=('bold',20),highlightcolor= "black" , highlightbackground= "black",command=lambda: self.SearchDatabase(window))

        self.Invalid = tk.Label(window,text="Email or Phone Number already in\nuse. Would you like to change info?",font= ('Helvetica',20,'bold'))
        self.MainPageInterface(window)
    
    def MainPageInterface(self,window):
        self.title.place(x=90,y=30)
        self.Add.place(x=60,y=200)
        self.Change.place(x=400,y=200)
        self.Search.place(x=250,y=350)
    
    def AddCustomerInterface(self,window):
        self.title.place_forget()
        self.Add.place_forget()
        self.Change.place_forget()
        self.Search.place_forget()

        self.labels = (self.fnlabel,self.lnlabel,self.pnlabel,self.elabel,self.alabel,self.clabel,self.pClabel)
        self.entries = (self.fname,self.lname,self.phone,self.email,self.address,self.city,self.pCode)
        self.entriesDict = [['fname',''],['lname',''],['phone',''],['email',''],['address',''],['city',''],['pCode','']]

        self.AddLabel.grid(row=1,column=1,columnspan=4)

        for i in range(7):
            self.labels[i].grid(column=2,row=(i+2))
            self.entries[i].grid(column=3,row=(i+2))

        self.AddButton.grid(row=9,column=2,columnspan=2)

    def AddToDatabase(self,window):
        self.AddButton.grid_forget()
        self.AddLabel.grid_forget()

        for i in range(7):
            self.entriesDict[i][1] = self.entries[i].get().replace(' ','')
            self.labels[i].grid_forget()
            self.entries[i].grid_forget()

        try: #Ensure that only email matches one customer
            for i in range(7):
                assert self.entriesDict[i][1] != ''
            for i in listOfEmail:
                assert self.entriesDict[3][1] != i
            listOfEmail.append(self.entriesDict[3][1])
            try: #Ensure that only one phone number matches one customer
                assert self.entriesDict[2][1] != ''
                for i in listOfPhone:
                    assert self.entriesDict[2][1] != i
                listOfPhone.append(self.entriesDict[2][1])
                database.AddCustomerInfo(self.entriesDict)
                self.entriesDict = [['fname',''],['lname',''],['phone',''],['email',''],['address',''],['city',''],['pCode','']]
            except:
                print('phone number not working')
                listOfEmail.remove(self.entriesDict[3][1])
        except:
            print('email not working')
            #self.Invalid.place(50,100)
            
        self.MainPageInterface(window)
         
    def ChangeCustomerInterface(self,window):
        self.window = window
        self.title.place_forget()
        self.Add.place_forget()
        self.Change.place_forget()
        self.Search.place_forget()

    def SearchCustomerInterface(self,window):
        self.window = window
        self.title.place_forget()
        self.Add.place_forget()
        self.Change.place_forget()
        self.Search.place_forget()

        self.SearchLabel.grid(row=1,column=1,columnspan=4)
        
        for i in range(7):
            self.labels[i].grid(column=2,row=(i+2))
            self.entries[i].grid(column=3,row=(i+2))
        
        self.SearchButton.grid(row=9,column=2,columnspan=2)

    def SearchDatabase(self,window):
        self.SearchLabel.grid_forget()
        self.AddLabel.grid_forget()

        for i in range(7):
            self.entriesDict[i][1] = self.entries[i].get().replace(' ','') #Creates a list
            self.labels[i].grid_forget()
            self.entries[i].grid_forget()
        print(self.entriesDict)
        self.SearchButton.grid_forget()
        database.SearchCustomerInfo(self.entriesDict)
        self.MainPageInterface(window)

class DatabaseMods:
    def __init__(self,file):
        self.connection = sqlite3.connect(file)
        self.cursor = self.connection.cursor()

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
        self.cursor.execute(qCustomerInfoCreation)
        self.r3 = self.cursor.fetchall()

        qPetInfoCreation = """
        create table if not exists petInfo (
            id integer primary key autoincrement,
            petName tinytext,
            type tinytext,
            breed tinytext,
            birthdate date,
            ownerID tinytext);
        """
        self.cursor.execute(qPetInfoCreation)
        self.r3 = self.cursor.fetchall()

        qVisitsCreation = """
        create table if not exists visits (
            id integer primary key autoincrement,
            ownerID tinytext,
            petID tinytext,
            details text,
            cost tinyint,
            paid tinyint);
        """
        self.cursor.execute(qVisitsCreation)
        self.r3 = self.cursor.fetchall()

        qTables = "SELECT name FROM sqlite_master WHERE type='table';"
        self.cursor.execute(qTables)
        self.r3 = self.cursor.fetchall()
        
        self.cursor.execute('PRAGMA table_info(vetcustomersinfo);')
        self.r3 = self.cursor.fetchall()
        print(self.r3)

    def AddCustomerInfo(self,list):
        self.list = list
        qAdd = f"insert into vetcustomersinfo (fname,lname,phone,email,address,city,pCode) values ('{self.list[0][1]}','{self.list[1][1]}','{self.list[2][1]}','{self.list[3][1]}','{self.list[4][1]}','{self.list[5][1]}','{self.list[6][1]}');"
        self.cursor.execute(qAdd)
        self.connection.commit()
        self.A = self.cursor.fetchall()
        print(self.A,'Input Complete\n')

    def SearchCustomerInfo(self,list):
        self.list = list
        queryText = ''
        for i in self.list:
            if i[1] != '':
                queryText = queryText + ' ' + i[0] + ' = ' + i[1] + ' and'
        if queryText != '':
            try:
                queryText = queryText.removesuffix(' and')
                qSearch = f'SELECT * FROM vetcustomersinfo where' + queryText
                print(qSearch)
                self.cursor.execute(qSearch)
                self.connection.commit()
                self.S = self.cursor.fetchall()
                print(self.S)
                self.S = ''
                for i in self.S:
                    print(i,self.S)
            except:
                print(self.S)

    def ChangeCustomerInfo(self,list):
            pass
                        

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


window1 = tk.Tk()
window1.minsize(800,800)
db = 'dbase.db'
database = DatabaseMods(db)
gui = WindowInterface(window1)
window1.mainloop()