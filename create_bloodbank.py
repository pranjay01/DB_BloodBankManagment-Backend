import mysql.connector as mysql
from mysql.connector import errorcode


def get_connection():
    try:

        db = mysql.connect(
        host = "localhost",
        user = "root",
        passwd = "P@ssw0rD",
        database = "Blood_Donation_Project"
        )
    except mysql.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Incorrect usernasme or password")
            #return ("error token : ")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
            #return ("error token : ")
        else:
            print(err)
            #return ("error token : ")
    return db

create_blood_bank_query = """CREATE TABLE IF NOT EXISTS BLOOD_BANK (Bbank_id INT NOT NULL ,
                              Name VARCHAR(45)  NOT NULL, 
                              Type VARCHAR(15),
                              phone_no BIGINT NOT NULL CHECK (phone_no BETWEEN 1000000000 and 9999999999));"""
    
add_primary_key_bloodbank_query = """ALTER TABLE BLOOD_BANK ADD CONSTRAINT Pk_Bloodbank 
                                 PRIMARY KEY AUTO_INCREMENT (Bbank_id)"""

autoincrement_blood_bank_table = """ALTER TABLE BLOOD_BANK MODIFY Bbank_id INTEGER NOT NULL AUTO_INCREMENT """


def drop_table(cursor,tname):
    cursor.execute('DROP TABLE IF EXISTS {}',format(tname))

    
def create_table(cursor,query):
    try:
        cursor.execute(query)
    except mysql.Error as err:
        print("Schema creation failed: {}".format(err))
        exit(1)    
        
def add_pk(cursor,query):
    try:
        cursor.execute(query)
    except mysql.Error as err:
        print("Primar key addition failed: {}".format(err))
        exit(1)    

def add_constraint_auto_increment(cursor,query):
    try:
        cursor.execute(query)
    except mysql.Error as err:
        print("Auto increment addition failed: {}".format(err))
        exit(1)    


if __name__ == '__main__':  # to not run code on import
    db=get_connection()
    cursor = db.cursor()

    drop_table(cursor,"BLOOD_BANK")
    
    create_table(cursor,create_blood_bank_query)
    add_pk(cursor,add_primary_key_bloodbank_query)
    add_constraint_auto_increment(cursor,autoincrement_blood_bank_table)

    db.commit()
    db.close()
