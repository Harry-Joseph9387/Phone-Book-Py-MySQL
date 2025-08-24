print(''' WELCOME TO PHONE BOOK DIRECTORY
                TO START AN OPTION BELOW , TYPE THE OPTION NO.
                    (1)To add a new contact
                    (2)To delete an existing contact
                    (3)To view a specific contact
                    (4)To edit a contact''')

import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='user1')
mycursor=mydb.cursor()

question=input("is this your first time using this program? y/n")
if question.lower()=='y':
    print("OK,The phone book is created")
    mycursor.execute('create database PHONEBOOK')
    mycursor.execute('use PHONEBOOK')
    mycursor.execute('create table contents(SLNO integer(2),phonenum integer(10),name varchar(20),address varchar(100),email varchar (50))')
else:
    print("Ok")

mycursor.execute('use PHONEBOOK')


wish=int(input('type here: '))



if wish==1:
    i=1
    while True:
        name=input('enter the name: ')
        address=input('address: ')
        phone=int(input('enter phone no. : '))
        email=input('enter email: ')
        sett=(i,phone,name,address,email)

        
        i+=1

        
        command=("insert into contents values(%s,%s,%s,%s,%s)")
        mycursor.execute(command,sett)
        mydb.commit()

        
        r=input('got more contacts to add?  y/n ')
        if r.lower()=='n':
            break
        print("The details are added")

    
elif  wish==2:
    i=1
    while True:
        phone=int(input('enter the phone number whose contact details is to be deleted: '))
        sett=(phone,)
        command=("delete from contents where phonenum=%s")

        
        mycursor.execute(command,sett)

        
        mydb.commit()
        
        
        print("Contact having phone number",phone,"is deleted ")
        r=input("continue? y/n")
        if r.lower()=='n':
            break
    
elif wish==3:
    while True:
        contact_name=input("Enter name to view the person's contact")
        command=("select * from contents where name=%s ")
        sett=(contact_name,)
        mycursor.execute(command,sett)
        
        
        for i in mycursor:
            x=list(i)
            print('Name: ',x[2])
            print('phone number: ',x[1])
            print('address: ',x[3])
            print('email: ',x[4])

        

        r=input("continue? y/n")
        if r.lower()=='n':
            break


elif wish==4:
    while True:
        print('''WHAT YOU WANT TO CHANGE?
                  (1)Email
                  (2)Name
                  (3)Phone no.
                  (4)Address''')
        x=int(input("Enter the option no."))
        contact_name=input("Enter Name of the contact")

        if x==1:
            new_email=input("Enter your new email: ")
            command="update contents set email=%s where name=%s"
            y=(new_email,contact_name)
            print("The new email is added")
            
            

        elif x==2:
            new_name=input("Enter a new name: ")
            command="update contents set name=%s where name=%s"
            y=(new_name,contact_name)
            print("The new name is added")
            
        

        elif x==3:
             new_phonenum=int(input("Enter the new Phone no. : "))
             command="update contents set phonenum=%s where name=%s"
             y=(new_phonenum,contact_name)
             print("The new Phone no. is added")

             
        elif x==4:
             new_address=input("Enter your new address: ")
             command="update contents set address=%s where name=%s"
             y=(command,new_address)
             print("The new address is added")

        else:
            print("No such option no.")
         
        mycursor.execute(command,y)        
        mydb.commit()            
        r=input("\n continue? y/n")
        if r.lower()=='n':
            break         
