
import mysql.connector as mysql
from connection import get_connection


db=get_connection()
cursor = db.cursor()
#select_query="SELECT Blood_id, Blood_Group, Donor_id, Donation_Date, Date_of_Expiry, Special_Attributes \
                #            FROM BLOOD \
                #            WHERE Br_id=%s AND Blood_Group='%s'"
select_query = f"""SELECT Blood_id, Blood_Group, Donor_id, Donation_Date, Date_of_Expiry, Special_Attributes 
                     FROM BLOOD WHERE Br_id={1} AND Blood_Group={2}"""            

try:
    cursor.execute(select_query)#,(parameters["Br_id"],parameters["Blood_Group"]))

    result  = cursor.fetchall()
    print(result)

except mysql.Error as err:
        print("Internal Server error: {}".format(err))
