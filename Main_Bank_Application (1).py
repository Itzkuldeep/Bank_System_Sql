#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# # Requirments:
#     Bank Application 
#     1. Login
#     Ask Account number and password 
#     if accno and password is correct then
#     1. credit
#     2. debit
#     3. change password
#         password should be valid
#             a. It should be 8 char long atleast be.
#             b. At Least 1 number, 1 upper case, 1 lower case and 1 sp char
#     4. check balance
#     5. Show details
#     6. logout 
#     else
#        No not allow to login
#      2. Signup
#              Take new data as input
#             1. username
#             2. password
#                     password should be valid 
#                         a. It should be 8 char long atleast
#                         b. Atleast 1 number, 1 upper case, 1 lower case and 1 sp char
#             3. Initial Balance
#                     it should be >= 2000
#               Generate account number in serial order 
#               like in this case it should be 1004 
#      3. Forgot password 
#      4. Exit

# # Importing Libraries

# In[19]:


from getpass import getpass
import pymysql as sql
import os
import math
import random
import smtplib


# # Password Validation

# In[2]:


def passkey(password):
        
    lower= 0
    upper=0
    special = 0
    digit = 0
    
    for char in password:
        if char.isdigit():
            digit += 1
        elif char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif not char.isidentifier():
            special += 1
        
    if lower>=1 and upper>=1 and digit>=1 and special>=1 and len(password)>=8:
        return True
    else:
        return False


# # OTP 
# 

# In[70]:


def otp12():
    srvr = sql.connect(user="root", host="localhost", password="", port=3306, database="python1pm")
    crsr = srvr.cursor()
    cmd2 = f"select acc_no from bank_data where acc_no ={new_acc}"
    crsr.execute(cmd2)
    data1 = crsr.fetchone()
    val = data1[0]
    
    digits="0123456789"
    OTP=""
    for i in range(6):
        OTP+=digits[math.floor(random.random()*10)]
    otp = OTP + " is your OTP"
    msg= otp
    
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("kuldeepsinghtak10@gmail.com", "fmlekqacqtuadnsd")
    emailid = input("Enter your email: ")
    s.sendmail('&&&&&&&&&&&',emailid,msg)
    a = input("Enter Your OTP >>: ")
    if a == OTP:
        print("Verified")
        new_password = getpass("Enter New Password: ")
        if passkey(new_password):
            new1 = f"update bank_data set password = '{new_password}' where acc_no = {new_acc}"
            crsr.execute(new1)
            srvr.commit()
            print("Password Updated")
        else:
            print("Invalid password format. Password must be at least 8 characters long and contain at least one number, one uppercase letter, one lowercase letter, and one special character")
    else:
        print("Please Check your OTP again")


# In[ ]:





# # Server Connectivity

# In[62]:


def db_connect():
    srvr = sql.connect(user='root', password='', host='localhost', port=3306, database='Python1pm')
    crsr = srvr.cursor()
    return srvr,crsr


# In[ ]:





# # Signup

# In[63]:


def signup():
    username = input("Enter Username: ")
    password = getpass("Enter Password: ")
    
    if passkey(password):
        print("Password is valid.... ")
        
        print("Initial amount of 2000 is required to open an account: ")
        choice = input("Enter your choice (y/n)").lower()
        
        if choice == "y":
            srvr, crsr = db_connect()
            cmd = "select acc_no from bank_data order by acc_no desc limit 1"
            crsr.execute(cmd)
            data = crsr.fetchall()
            new_acc = data[0][0] + 1
            balance = 2000
            cmd1 = f"insert into bank_data values({new_acc}, '{username}', '{password}', {balance})"
            crsr.execute(cmd1)
            srvr.commit()
            print("Your accoutn is Created...")
            print(f"Your account number is {new_acc}")
            srvr.close()
            
        else:
            print("Initial Balance of 2000 is Required, Thank You for giving us your time.")
    else:
        print("Password is not valid, Try Again!")


# In[ ]:





# # Login

# In[73]:


def login():
    new_acc = int(input('Enter Account Number'))
    password = getpass("Enter Password: ")
    
    
    srvr = sql.connect(user="root", host="localhost", password="", port=3306, database="python1pm")
    crsr = srvr.cursor()
    cmd2 = f"select * from bank_data where acc_no ={new_acc}"
    crsr.execute(cmd2)
    data1 = crsr.fetchone()
    
    value = data1[3]
    user = data1[1]
    
    if new_acc == data1[0] and password == data1[2]:
        while True:
            
            print(f"\nLogged in as {user}")
            print("1. Credit")
            print("2. Debit")
            print("3. Change Password")
            print("4. Check Balance")
            print("5. Show Details")
            print("6. Logout")
            
            choice1 = input("Enter your choice: ")
            
            if choice1 == '1':
                amount = int(input('Enter amount to Credit: '))
                value += amount
                new = f"update bank_data set balance = {value} where acc_no = {new_acc}"
                crsr.execute(new)
                srvr.commit()
                print(f'Balance Updated, New Balance is {value}')
                
                
            elif choice1 == '2':
                amount = int(input('Enter amount to Debit: '))
                if amount <= value:
                    value -= amount
                    new = f"update bank_data set balance = {value} where acc_no = {new_acc}"
                    crsr.execute(new)
                    srvr.commit()
                    print(f'Debit successful. New balance: {value}')
                else:
                    print("Insufficient Balance")
                    
            elif choice1 == '3':
                digits="0123456789"
                OTP=""
                for i in range(6):
                    OTP+=digits[math.floor(random.random()*10)]
                otp = OTP + " is your OTP"
                msg= otp
                
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                s.login("kuldeepsinghtak10@gmail.com", "fmlekqacqtuadnsd")
                emailid = input("Enter your email: ")
                s.sendmail('&&&&&&&&&&&',emailid,msg)
                a = input("Enter Your OTP >>: ")
                if a == OTP:
                    print("Verified")
                    new_password = getpass("Enter New Password: ")
                    if passkey(new_password):
                        new1 = f"update bank_data set password = '{new_password}' where acc_no = {new_acc}"
                        crsr.execute(new1)
                        srvr.commit()
                        print("Password Updated")
                    else:
                        print("Invalid password format. Password must be at least 8 characters long and contain at least one number, one uppercase letter, one lowercase letter, and one special character")
                else:
                    print("Please Check your OTP again")
                
            elif choice1 == '4':
                print(f'Current Balance is {value}')
            
            elif choice1 == '5':
                print(f'Account Number = {new_acc}\n User Name = {user}\n Balance = {value}')
            
            elif choice1 == '6':
                print("Logging Out, Thank You for service")
                break;
                
    else:
        print("Invalid account number or password. Please try again.")


# # Forgot Password

# In[76]:


def Fgpass():
    new_acc = int(input('Enter Account Number'))    
    current_pass = getpass("Enter Old Password: ")
    
    srvr = sql.connect(user="root", host="localhost", password="", port=3306, database="python1pm")
    crsr = srvr.cursor()
    cmd2 = f"select * from bank_data where acc_no ={new_acc}"
    crsr.execute(cmd2)
    data1 = crsr.fetchone()
    value = data1[2]


    while True:
        if current_pass == value:
            print(f"Your Given Password is Correct")
            break
        elif current_pass != value:
            print("Old password is Wrong!")
        
            choice = input("Enter Your choice is you want to Edit Password or Not (y/n)").lower()
            if choice == 'y':
                digits="0123456789"
                OTP=""
                for i in range(6):
                    OTP+=digits[math.floor(random.random()*10)]
                otp = OTP + " is your OTP"
                msg= otp
                
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                s.login("kuldeepsinghtak10@gmail.com", "fmlekqacqtuadnsd")
                emailid = input("Enter your email: ")
                s.sendmail('&&&&&&&&&&&',emailid,msg)
                a = input("Enter Your OTP >>: ")
                if a == OTP:
                    print("Verified")
                    new_password = getpass("Enter New Password: ")
                    if passkey(new_password):
                        new1 = f"update bank_data set password = '{new_password}' where acc_no = {new_acc}"
                        crsr.execute(new1)
                        srvr.commit()
                        print("Password Updated")
                        break;
                    else:
                        print("Invalid password format. Password must be at least 8 characters long and contain at least one number, one uppercase letter, one lowercase letter, and one special character")
                else:
                    print("Please Check your OTP again")
                
        elif choice == "n":
            break;


# # Exit

# In[ ]:


def exit():
    srvr = sql.connect(user="root", host="localhost", password="", port=3306, database="python1pm")
    crsr = srvr.cursor()
    print("Exiting System!")
    srvr.close()


# In[77]:


print('\t----------------Bank System----------------\t')
try:
    while True:
        print('\n\t')
        print('1: SignUp')
        print('2: Login')
        print('3: Forgot Password')
        print('4: Exit')
        choice = input("Choose What to do...")
        
        if choice == '1':
            print('Signing into System...')
            signup()
        elif choice == '2':
            print('Loging into System...')
            login()
        elif choice == '3':
            print('Forgot Password !?')
            Fgpass()
        elif choice == '4':
            print('Exiting from System...')
            exit()
            break
        else:
            print('Error code: x000043B2')
            print('Invalid Error')
except Exception as e:
    print("Continue you Work....")
    while True:
        print('\n\t')
        print('1: SignUp')
        print('2: Login')
        print('3: Forgot Password')
        print('4: Exit')
        choice = input("Choose What to do...")
    
        if choice == '1':
            print('Signing into System...')
            signup()
        elif choice == '2':
            print('Loging into System...')
            login()
        elif choice == '3':
            print('Forgot Password !?')
            Fgpass()
        elif choice == '4':
            print('Exiting from System...')
            exit()
            break
        else:
            print('Error code: x000043B2')
            print('Invalid Error')
        


# In[ ]:





# In[ ]:




