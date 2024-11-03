#**************************************************#


#################MAIN MENU PAGE########################


#*************************************************#


import tkinter
import sqlite3
import tkinter.messagebox
from patients_data import P_display
from patients_data import D_display
from patients_data import P_UPDATE
from employee_reg import emp_screen
from appointment import appo

conn=sqlite3.connect("data.db")
print("DATABASE CONNECTION SUCCESSFUL")

#variables
root1=None
rootp=None
pat_ID=None
pat_name=None
pat_dob=None
pat_address=None
pat_sex=None
pat_BG=None
pat_email=None
pat_contact=None
pat_contactalt=None
pat_CT=None


#EXIT for MENU
def ex():
    global root1
    root1.destroy()

#MENU BUTTONS
def menu():
    global root1,button1,button2,button3,button4,button5,m,button6
    root1=tkinter.Tk()
    root1.geometry("380x500")
    root1.title("Hospital Management System")
    root1.configure(background="white")
    root1.resizable(height = False,width = False)
    menubar1=tkinter.Menu(root1)
    helpmenu1=tkinter.Menu(menubar1,tearoff=0)
    helpmenu1.add_command(label="Help",command=helpmessage)
    helpmenu1.add_command(label="About",command=aboutmessage)
   #menubar1.add_cascade(label="File", menu=filemenu)
    menubar1.add_cascade(label="Options", menu=helpmenu1)
    root1.config(menu=menubar1)
   # m=tkinter.Label(root1,text="",font='Times 16 bold italic',fg='grey')
    button1=tkinter.Button(root1,text="PATIENT REGISTRATION",command=PAT,bg='light blue',fg='black',pady="20")
   # button2 = tkinter.Button(root1, text="ROOM ALLOCATION",bg='light green',fg='black',command=Room_all,pady="20")
    button3 = tkinter.Button(root1, text="EMPLOYEE REGISTRATION",bg='light blue',fg='black',command=emp_screen,pady="20")
    button4 = tkinter.Button(root1, text="BOOK APPOINTMENT",bg='light green',fg='black',command=appo,pady="20")
    #button5 = tkinter.Button(root1, text="PATIENT BILL",bg='light blue',fg='black',command=BILLING,pady="20")
    #button6 = tkinter.Button(root1, text="EXIT",command=ex,bg='light green',fg='black',pady="20")
    #m.place(x=75,y=5)
    button1.pack(side=tkinter.TOP)
    button1.place(x=80,y=30)
    #button2.pack(side=tkinter.TOP)
    #button2.place(x=80,y=130)
    button3.pack(side=tkinter.TOP)
    button3.place(x=80,y=130)
    button4.pack(side=tkinter.TOP)
    button4.place(x=80, y=230)
    #button5.pack(side=tkinter.TOP)
    #button5.place(x=80,y=330)
    #button6.pack(side=tkinter.TOP)
    #button6.place(x=80,y=530)
    root1.mainloop()

p=None
#input patient form
def IN_PAT():
    global pp1, pp2, pp3, pp4, pp5, pp6, pp7, pp8, pp9, pp10,ce1,conn
    conn=sqlite3.connect("data.db")
    conn.cursor()
    pp1=pat_ID.get()
    pp2=pat_name.get()
    pp3=pat_sex.get()
    pp4=pat_BG.get()
    pp5=pat_dob.get()
    pp6=pat_contact.get()
    pp7=pat_contactalt.get()
    pp8=pat_address.get()
    pp9=pat_CT.get()
    pp10=pat_email.get()
    if pp1 == " " or pp2 == " " or pp3 == " " or pp4 == " " or pp4 == " " or pp6 == " " or pp7 == " " or pp8 == " " or pp9 == " " or pp10 == " ":
        conn.execute('INSERT INTO PATIENT VALUES(?,?,?,?,?,?,?,?)',(pp1,pp2,pp3,pp4,pp5,pp8,pp9,pp10,))
        conn.execute('INSERT INTO CONTACT_NO VALUES (?,?,?)',(pp1,pp6,pp7,))
        tkinter.messagebox.showinfo("DATABSE SYSTEM","DETAILS INSERTED INTO DATABASE")
        conn.commit()
    else:
        tkinter.messagebox.showwarning("DATABASE SYSTEM","PLEASE ENTER SOME DATA")


#exit from patient form
def EXO():
    rootp.destroy()

#function for patient form help
def helpmessage():
    tkinter.messagebox.showinfo("Help","Contact DBA")

def aboutmessage():
    tkinter.messagebox.showinfo("About","Made by Satyam Kumar Verman")

#PATIENT FORM
back=None
SEARCH=None
DELETE=None
UPDATE=None

def PAT():
    global pat_address, pat_BG, pat_contact, pat_contactalt, pat_CT, pat_dob, pat_email, pat_ID, pat_name, pat_sex
    global rootp,regform,id,name,dob,sex,email,ct,addr,c1,c2,bg,SUBMIT,menubar,filemenu,back,SEARCH,DELETE,UPDATE
    rootp=tkinter.Tk()
    rootp.title("REGISTRATION")
    rootp.configure(background="white")
    rootp.resizable(height = False,width = False)
    menubar=tkinter.Menu(rootp)
    filemenu=tkinter.Menu(menubar,tearoff=0)
    filemenu.add_command(label="NEW",command=PAT)
    filemenu.add_separator()
    filemenu.add_command(label="EXIT", command=EXO)
    helpmenu=tkinter.Menu(menubar,tearoff=0)
    helpmenu.add_command(label="HELP",command=helpmessage)
    helpmenu.add_command(label="ABOUT",command=aboutmessage)
    menubar.add_cascade(label="File", menu=filemenu)
    menubar.add_cascade(label="Help", menu=helpmenu)
    rootp.config(menu=menubar)
    regform=tkinter.Label(rootp,text="REGISTRATION",font="Arial 16 bold",bg="white",fg="grey")
    id=tkinter.Label(rootp,text="PATIENT ID",bg="white")
    pat_ID=tkinter.Entry(rootp)
    name=tkinter.Label(rootp,text="PATIENT NAME",bg="white")
    pat_name = tkinter.Entry(rootp)
    sex=tkinter.Label(rootp,text="GENDER",bg="white")
    pat_sex=tkinter.Entry(rootp)
    dob=tkinter.Label(rootp, text="DOB (YYYY-MM-DD)",bg="white")
    pat_dob=tkinter.Entry(rootp)
    bg=tkinter.Label(rootp, text="BLOOD GROUP",bg="white")
    pat_BG=tkinter.Entry(rootp)
    c1=tkinter.Label(rootp, text="CONTACT NUMBER",bg="white")
    pat_contact=tkinter.Entry(rootp)
    c2=tkinter.Label(rootp, text="ALTERNATE CONTACT",bg="white")
    pat_contactalt=tkinter.Entry(rootp)
    email=tkinter.Label(rootp, text="EMAIL",bg="white")
    pat_email = tkinter.Entry(rootp)
    ct=tkinter.Label(rootp,text="DOCTOR",bg="white")
    pat_CT=tkinter.Entry(rootp)
    addr=tkinter.Label(rootp, text="ADDRESS",bg="white")
    pat_address=tkinter.Entry(rootp)
    back=tkinter.Button(rootp,text="  BACK  ",command=menu)
    SEARCH=tkinter.Button(rootp,text="  SEARCH  ",command=P_display)
    DELETE=tkinter.Button(rootp,text="  DELETE  ",command=D_display)
    UPDATE=tkinter.Button(rootp,text="  UPDATE  ",command=P_UPDATE)
    SUBMIT=tkinter.Button(rootp,text="  SUBMIT  ",command=IN_PAT,)
    regform.pack()
    id.pack()
    pat_ID.pack()
    name.pack()
    pat_name.pack()
    sex.pack()
    pat_sex.pack()
    dob.pack()
    pat_dob.pack()
    bg.pack()
    pat_BG.pack()
    c1.pack()
    pat_contact.pack()
    c2.pack()
    pat_contactalt.pack()
    email.pack()
    pat_email.pack()
    ct.pack()
    pat_CT.pack()
    addr.pack()
    pat_address.pack()
    SUBMIT.pack()
    back.pack(side=tkinter.LEFT)
    UPDATE.pack(side=tkinter.LEFT)
    DELETE.pack(side=tkinter.LEFT)
    SEARCH.pack(side=tkinter.LEFT)
    rootp.mainloop()

