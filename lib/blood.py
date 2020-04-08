import mysql.connector as mysql
from create_table import get_connection
from datetime import datetime

datetime.today().strftime('%Y-%m-%d')


class Blood:

    @classmethod
    def insert_blood(self,bloodUnit):
        db=get_connection()
        cursor = db.cursor()

        date=datetime.today().strftime('%Y-%m-%d')
        insert_query="INSERT INTO BLOOD (Blood_Group,Br_id,Donor_id,Donation_Date,Special_Attributes)  VALUES (%s,%s,%s,%s,%s)"
        cursor.execute(insert_query,(bloodUnit['bl_grp'], \
        bloodUnit['br_id'], bloodUnit['dnr_id'],date,bloodUnit['spcl_attr']))

        db.commit()
        db.close()
        return "success"


     