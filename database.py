#**************************************************#


#################DATABASE FILES########################


#*************************************************#

import sqlite3
connection=sqlite3.connect("data.db")
print("DATABASE CONNNECTION SUCCESSFUL")

#tables used in this project
#1)patient - for managing patient details
#2)contact_no - for managing contact details
#3)employee - for managing employee details
#4)appointment - for managing appointents

connection.execute("Drop table if EXISTS PATIENT")
connection.execute("Drop table if EXISTS CONTACT_NO")
connection.execute("DROP TABLE if EXISTS employee")
connection.execute("DROP TABLE if EXISTS appointment")

connection.execute("""Create table PATIENT
           (PATIENT_ID int(10) primary key,
             NAME VARCHAR(20) not null,
             GENDER varchar(10) not null,
             BLOOD_GROUP varchar(5) not null,
             DOB date not null,
             ADDRESS varcahr(100) not null,
             CONSULT_TEAM varchar(50) not null,
             EMAIL varchar(20) not null
             )""")
print("PATIENT TABLE CREATED SUCCESSFULLY")
connection.execute("""CREATE TABLE CONTACT_NO
           (PATIENT_ID int(10) PRIMARY KEY,
             CONTACTNO int(15) not null,
             ALT_CONTACT int(15),
             FOREIGN KEY(PATIENT_ID) REFERENCES PATIENT(PATIENT_ID))
            """)
print("CONTACT TABLE CREATED SUCCESSFULLY")






connection.execute("""create table employee
            (EMP_ID varchar(10) primary key,
             EMP_NAME varchar(20)not null,
             SEX varchar(10) not null,
            AGE int(5) not null,
             DESIG varchar(20) not null,
             SAL float(10) not null,
             EXP varchar(100) not null,
             EMAIL varcahr(20) not null,
             PHONE int(12))""")

print ("EMPLOYEE TABLE CREATED SUCESSFULLY")


connection.execute("""create table appointment
            (
             PATIENT_ID int(20) not null,
             EMP_ID varchar(10) not null,
             AP_NO varchar(10) primary key,
             AP_TIME time,
             AP_DATE date,
             description varchar(100),
            foreign key(PATIENT_ID) references patient(PATIENT_ID),
            foreign key(EMP_ID) references doctor(EMP_ID));""")

print("APPOINTMENT TABLE CREATED SUCCESSFULLY")



connection.close()