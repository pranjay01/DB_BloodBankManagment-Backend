#SJSU CMPE 138Spring2020 TEAM7

# To create DB Tables for Donor, Donor_email, Donor_phone, EMERGENCY_CONTACT_INFO, EMERGENCY_CONTACT_EMAIL

import mysql.connector 
from mysql.connector import errorcode
from connection import get_connection


# def get_connection(uname,upassword):
#     try:
#         db = mysql.connector.connect (
#             host = "localhost",
#             user = uname,
#             passwd = upassword,
#             database = "company2")

#     except mysql.connector.Error as err:
#         if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#             print("Something is wrong with your user name or password")
#             #return ("error token : ")
#         elif err.errno == errorcode.ER_BAD_DB_ERROR:
#             print("Database does not exist")
#             #return ("error token : ")
#         else:
#             print(err)
#             #return ("error token : ")
#     return db

def query_string(table_name):

    if table_name == 'OPERATOR':
        create_table = """CREATE TABLE IF NOT EXISTS OPERATOR (
        Operator_id INT NOT NULL AUTO_INCREMENT,
        PRIMARY KEY (Operator_id));"""
    
    elif table_name == 'DONOR':
        create_table = """CREATE TABLE IF NOT EXISTS DONOR(
            Donor_id INT NOT NULL AUTO_INCREMENT, 
            Name VARCHAR(25) NOT NULL,
            Blood_group ENUM('O+','A+','B+','AB+','O-','A-','B-','AB-') NOT NULL,
            Street VARCHAR(20),
            City VARCHAR(20),
            Zip INT CHECK (Zip BETWEEN 10000 and 99999),
            Paid_Unpaid BOOL DEFAULT false,
            Notification_Subscription BOOL DEFAULT false,
            Notification_Type ENUM('MAIL','MESSAGE') ,
            Operator_id INT ,
            PRIMARY KEY (Donor_id),
            FOREIGN KEY (Operator_id) references OPERATOR (Operator_id)
            ON DELETE SET NULL ON UPDATE CASCADE)"""

    elif table_name == 'DONOR_EMAIL' :
        create_table = """CREATE TABLE IF NOT EXISTS DONOR_EMAIL(
            Donor_id INT NOT NULL,
            Email_id VARCHAR(25) NOT NULL,
            PRIMARY KEY (Donor_id,Email_id),
            FOREIGN KEY (Donor_id) references DONOR (Donor_id)
            ON DELETE CASCADE ON UPDATE CASCADE);"""

    elif table_name == 'DONOR_PHONE' :
        create_table = """CREATE TABLE IF NOT EXISTS DONOR_PHONE(
            Phone_no BIGINT NOT NULL CHECK (phone_no BETWEEN 1000000000 and 9999999999),
            Donor_id INT NOT NULL,
            PRIMARY KEY (Donor_id,Phone_no),
            FOREIGN KEY (Donor_id) references DONOR (Donor_id)
            ON DELETE CASCADE ON UPDATE CASCADE);"""

    elif table_name == 'EMERGENCY_CONTACT_INFO' :
        create_table = """CREATE TABLE IF NOT EXISTS EMERGENCY_CONTACT_INFO(
            Phone_no BIGINT NOT NULL CHECK (phone_no BETWEEN 1000000000 and 9999999999),
            Donor_id INT NOT NULL,
            Name VARCHAR(25) NULL,
            PRIMARY KEY (Phone_no,Donor_id),
            FOREIGN KEY (Donor_id) references DONOR (Donor_id)
            ON DELETE CASCADE ON UPDATE CASCADE);"""

    elif table_name == 'EMERGENCY_CONTACT_EMAIL' :
        create_table = """CREATE TABLE IF NOT EXISTS EMERGENCY_CONTACT_EMAIL(
            Phone_no BIGINT NOT NULL,
            Donor_id INT NOT NULL,
            Email_id VARCHAR(25) NOT NULL,
            PRIMARY KEY (Phone_no,Donor_id,Email_id),
            FOREIGN KEY (Donor_id,Phone_no) references EMERGENCY_CONTACT_INFO (Donor_id,Phone_no)
            ON DELETE CASCADE ON UPDATE CASCADE);"""

    else :
        print('Incorrect table name')
        
    return create_table

def create_table_function(cursor,table_name):
    s = query_string(table_name)
    try:
        cursor.execute(s)
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

def drop_table(cursor,tname):
    cursor.execute(f'DROP TABLE IF EXISTS {tname}')

if __name__ == '__main__':  # to not run code on import
    db= get_connection()
    mycursor = db.cursor()
    drop_table(mycursor,'EMERGENCY_CONTACT_EMAIL')
    drop_table(mycursor,'EMERGENCY_CONTACT_INFO')
    drop_table(mycursor,'DONOR_PHONE')
    drop_table(mycursor,'DONOR_EMAIL')
    drop_table(mycursor,'DONOR')
    drop_table(mycursor,'OPERATOR')

    create_table_function(mycursor,'OPERATOR')
    create_table_function(mycursor,'DONOR')
    create_table_function(mycursor,'DONOR_EMAIL')
    create_table_function(mycursor,'DONOR_PHONE')
    create_table_function(mycursor,'EMERGENCY_CONTACT_INFO')
    create_table_function(mycursor,'EMERGENCY_CONTACT_EMAIL')

    db.close()