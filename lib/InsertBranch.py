#SJSU CMPE 138Spring2020 TEAM7

import mysql.connector as mysql
from connection import get_connection

class InsertInTable:

    @classmethod
    def branch(self, single_branch):
        db = get_connection()
        cursor = db.cursor()
        insert_query = """INSERT INTO BRANCH
        (Br_id,Br_Type,Bbank_id,Street,City,Zip)
        VALUES (%s,%s,%s,%s,%s)"""

        t = (single_branch['Br_id'], single_branch['Br_Type'], single_branch['Bbank_id'],
             single_branch['Street'], single_branch['City'], single_branch['Zip'])
        try:
            cursor.execute(insert_query, t)
            db.commit()
        except mysql.Error as err:
            print("Failed to add entry: {}".format(err))
            return {"status": 400, "entry": str(err)}
        db.close()
        return {"status": 200, "entry": single_branch}

class UpdateInTable:

    @classmethod
    def branch(self, single_branch):
        db = get_connection()
        # prepare query and data
        update_query = """ UPDATE BRANCH SET  Br_Type = %s, Bbank_id = %s, Street = %s, City = %s, Zip = %s WHERE  Br_id = %s """
        data = (single_branch['Br_Type'], single_branch['Bbank_id'],
             single_branch['Street'], single_branch['City'], single_branch['Zip'], single_branch['Br_id'])
        try:
            cursor = db.cursor()
            cursor.execute(update_query,data)
            db.commit()
        except mysql.Error as err:
            print("Failed to update entry: {}".format(err))
            return {"status": 400, "entry": str(err)}
        db.close()
        return {"status": 200, "entry": single_branch }
class DeleteInTable:

    @classmethod
    def branch(self, single_branch):
        db = get_connection()
        cursor = db.cursor()
        insert_query = f"DELETE FROM BRANCH WHERE Br_id = '{single_branch['Br_id']}'"
        try:
            cursor.execute(insert_query)
            db.commit()
        except mysql.Error as err:
            print("Failed to delete entry: {}".format(err))
            return {"status": 400, "entry": str(err)}
        db.close()
        return {"status": 200, "entry": single_branch}

class SelectInTable:

    @classmethod
    def branch(self, single_branch):
        db = get_connection()
        cursor = db.cursor(dictionary=True)

        try:
            cursor.execute(
                f"SELECT * FROM BRANCH WHERE Br_id = '{single_branch['Br_id']}'")
            mybranch = cursor.fetchall()
        except mysql.Error as err:
            print("Failed to get donor data: {}".format(err))
            return {"status": 400, "entry": str(err)}
        db.close()
        return {"status": 200, "entry": mybranch}