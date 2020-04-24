#SJSU CMPE 138Spring2020 TEAM7

import mysql.connector as mysql
from mysql.connector import errorcode


def get_connection():
    try:

        # This is for local db access
        # db = mysql.connect(
        #     host='localhost',
        #     user='root',
        #     passwd='Pranjay@01',
        #     database='Blood_Donation_Project',
        #     port=3307
        # )

        # For AWS db login uncomment the following, and comment the above
        db = mysql.connect(
        host = "bloodbankprod.cnlv0osh7hey.us-east-2.rds.amazonaws.com",
        user = "root",
        passwd = "bloodbank2020",
        database = "Blood_Donation_Project",
        port = 3306
        )
        return db
    except mysql.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
            return(err)
            # return ("error token : ")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
            return(err)
            # return ("error token : ")
        else:
            print(err)
            # return ("error token : ")
    
