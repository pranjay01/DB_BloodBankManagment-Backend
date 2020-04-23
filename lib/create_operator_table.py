#SJSU CMPE 138Spring2020 TEAM7

# To create DB Tables for OPERATOR, BLOOD_DONATION_EVENT...

import mysql.connector
from mysql.connector import errorcode
from connection import get_connection


# def get_connection(username, userpassword):
#     try:
#         db = mysql.connector.connect(
#             host="localhost",
#             user=username,
#             passwd=userpassword,
#             database="project")

#     except mysql.connector.Error as err:
#         if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#             print("Something is wrong with your user name or password")
#             # return ("error token : ")
#         elif err.errno == errorcode.ER_BAD_DB_ERROR:
#             print("Database does not exist")
#             # return ("error token : ")
#         else:
#             print(err)
#             # return ("error token : ")
#     return db


def query_string(table_name):
    if table_name == 'OPERATOR':
        create_table = """CREATE TABLE IF NOT EXISTS OPERATOR (
        Operator_id INT NOT NULL,
        Name VARCHAR(25)  NOT NULL,
        Email VARCHAR(25) NOT NULL,
        Password VARCHAR(20) NOT NULL,
        Bbank_id INT NOT NULL,
        PRIMARY KEY (Operator_id),
        FOREIGN KEY (Bbank_id) references BLOOD_BANK (Bbank_id)
        ON DELETE SET NULL ON UPDATE CASCADE)"""

    elif table_name == 'BLOOD_DONATION_EVENT':
        create_table = """CREATE TABLE IF NOT EXISTS BLOOD_DONATION_EVENT (
         Drive_id INT NOT NULL,
         Name VARCHAR(45)  NOT NULL,
         -- YYYY-MM-DD
         Date_of_event DATETIME NOT NULL,
         Venue VARCHAR(50) NOT NULL,
         Operator_id INT NOT NULL,
         PRIMARY KEY (Drive_id),
         FOREIGN KEY (Operator_id) references OPERATOR (Operator_id)
         ON DELETE SET NULL ON UPDATE CASCADE)"""
        
    else:
        print('Incorrect table name')

    return create_table


def create_table_function(cursor, table_name):
    s = query_string(table_name)
    try:
        cursor.execute(s)
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)


def drop_table(cursor, tname):
    cursor.execute(f'DROP TABLE IF EXISTS {tname}')


if __name__ == '__main__':  # to not run code on import
    db = get_connection()
    mycursor = db.cursor()

    drop_table(mycursor, 'OPERATOR')
    drop_table(mycursor, 'BLOOD_DONATION_DRIVE')


    create_table_function(mycursor, 'OPERATOR')
    create_table_function(mycursor, 'BLOOD_DONATION_DRIVE')

    db.close()