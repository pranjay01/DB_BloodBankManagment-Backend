#SJSU CMPE 138Spring2020 TEAM7

import mysql.connector as mysql
from mysql.connector import errorcode
from connection import get_connection


# def get_connection():
#     try:

#         # db = mysql.connect(
#         # host = "bloodbankprod.cnlv0osh7hey.us-east-2.rds.amazonaws.com",
#         # user = "root",
#         # passwd = "bloodbank2020",
#         # database = "bloodbankprod",
#         # port = 3306
#         db = mysql.connect(
#         host = "localhost",
#         user = "root",
#         passwd = "Pranjay@01",
#         database = "Blood_Donation_Project",
#         port = 3307
#         )
#     except mysql.Error as err:
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

create_blood_table_query = """CREATE TABLE IF NOT EXISTS BLOOD (Blood_id INT NOT NULL ,
                              Blood_Group ENUM('O+','A+','B+','AB+','O-','A-','B-','AB-') 
                              NOT NULL,
                              Br_id INT,
                              Donor_id INT ,
                              Donation_Date DATE NOT NULL,
                              Date_of_Expiry DATE GENERATED ALWAYS AS (DATE_ADD(Donation_Date, INTERVAL 2 MONTH)) ,
                              Special_Attributes VARCHAR(45))"""
    
add_primary_key_blood_query = """ALTER TABLE BLOOD ADD CONSTRAINT Pk_Blood 
                                 PRIMARY KEY AUTO_INCREMENT (Blood_id)"""

autoincrement_blood_table = """ALTER TABLE BLOOD MODIFY Blood_id INTEGER NOT NULL AUTO_INCREMENT """

blood_foreignkey_1 ="""ALTER TABLE BLOOD
                       ADD FOREIGN KEY (Br_id)
                       REFERENCES BRANCH (Br_id)
                       ON DELETE SET NULL
                       ON UPDATE CASCADE;"""

blood_foreignkey_2 = """ALTER TABLE BLOOD
                        ADD FOREIGN KEY (Donor_id)
                        REFERENCES DONOR (Donor_id)
                        ON DELETE SET NULL
                        ON UPDATE CASCADE;"""

create_blood_stock_query="""CREATE TABLE IF NOT EXISTS BLOOD_STOCK (
                            Br_id INT NOT NULL,
                            Blood_group VARCHAR(3) NOT NULL,
                            Btype_Limits INT DEFAULT 100)"""

add_primary_key_blood_stock_query="""ALTER TABLE BLOOD_STOCK ADD CONSTRAINT 
                                     PK_stock PRIMARY KEY (Br_id, Blood_group)"""

blood_stock_foreignkey="""ALTER TABLE BLOOD_STOCK
                          ADD FOREIGN KEY (Br_id)
                          REFERENCES BRANCH (Br_id)
                          ON DELETE CASCADE
                          ON UPDATE CASCADE;"""

def drop_table(cursor,tname):
    cursor.execute('DROP TABLE IF EXISTS {}',format(tname))

    
def create_table(cursor,query):
    try:
        cursor.execute(query)
    except mysql.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)    
        
def add_pk(cursor,query):
    try:
        cursor.execute(query)
    except mysql.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)    

def add_constraint_auto_increment(cursor,query):
    try:
        cursor.execute(query)
    except mysql.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)    


def add_fk(cursor,query):
    try:
        cursor.execute(query)
    except mysql.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)    


if __name__ == '__main__':  # to not run code on import
    db=get_connection()
    cursor = db.cursor()

    drop_table(cursor,"BLOOD")
    drop_table(cursor,"BLOOD_STOCK")

    create_table(cursor,create_blood_table_query)
    add_pk(cursor,add_primary_key_blood_query)
    add_constraint_auto_increment(cursor,autoincrement_blood_table)

    create_table(cursor,create_blood_stock_query)
    add_pk(cursor,add_primary_key_blood_stock_query)


    
    db.commit()
    db.close()
