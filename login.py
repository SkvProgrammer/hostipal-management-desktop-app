#**************************************************#


#################LOGIN PAGE########################


#*************************************************#


import tkinter
from window2 import menu
from tkinter import messagebox
import os
root=None
userbox=None
passbox=None
topframe=None
bottomframe=None
frame3=None
login=None
#command for login button
def GET():
    global userbox,passbox,error
    S1=userbox.get()
    S2=passbox.get()
    #filtering the data
    S1=S1.upper().strip()
    S2=S2.strip()
    #default usernames and passwords
    #set to
    # ->'satyam' and '12345' 
    # ->'rupesh'and '12345' 
    # ->'alok' and '12345'
    
    if(S1=='SATYAM' and S2=='12345'):
        menu()
    elif(S1=='ALOK' and S2=='12345'):
        menu()
    elif(S1=='RUPESH' and S2=='12345'):
        menu()
    elif(S1 == "" and S2 == ""):
        messagebox.showinfo("No Login Details are given","Please enter the login details")
    else:
        messagebox.showinfo("Login Details are Wrong","Please enter the correct details")


#LOGIN PAGE WINDOW
def Login():
    global userbox,passbox,login,topframe,bottomframe
    root = tkinter.Tk()
    root.configure(background="white")
    root.geometry("280x200")
    root.resizable(height=False,width=False)
    topframe = tkinter.Frame(root,bg="white")
    topframe.pack()
    bottomframe=tkinter.Frame(root,bg="white")
    bottomframe.pack()
    heading = tkinter.Label(topframe, text="LOGIN",bg='white',fg='grey',font='Times 16 bold')
    username=tkinter.Label(topframe,text="USERNAME",bg="white")
    userbox = tkinter.Entry(topframe)
    password=tkinter.Label(bottomframe,text="PASSWORD",bg="white")
    passbox = tkinter.Entry(bottomframe,show="*")
    login = tkinter.Button(bottomframe, text="LOGIN", command=GET,font="arial 8 bold")
    heading.pack()
    username.pack()
    userbox.pack()
    password.pack()
    passbox.pack()
    login.pack()
    root.title("LOGIN")
    root.mainloop()

#calling the function for the login page 
Login()

