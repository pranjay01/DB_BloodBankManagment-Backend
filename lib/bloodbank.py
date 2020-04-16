import mysql.connector as mysql
from create_table import get_connection



class Bloodbank:

    @classmethod
    def insert_bloodbank(self,bloodbank):
        db=get_connection()
        cursor = db.cursor()

        insert_query="INSERT INTO BLOOD_BANK (Bbank_id,Name,Type,Phone_No)  VALUES (%s,%s,%s,%s)"
        cursor.execute(insert_query,(bloodbank['Bbank_id'], \
        bloodbank['Name'],bloodbank['Type'],bloodbank['Phone_No']))

        db.commit()
        db.close()
        return "success"

    @classmethod
    def delete_bloodbank(self,bloodbank):
        db=get_connection()
        cursor = db.cursor()

        delete_query=f"DELETE FROM BLOOD_BANK WHERE Bbank_id = '{bloodbank['Bbank_id']}'"
        try:
            cursor.execute(delete_query)
            db.commit()
        except mysql.Error as err:
            print("Failed to delete entry: {}".format(err))
            return {"status": 400, "entry": str(err)}
        db.close()
        return {"status": 200, "entry": bloodbank}

    @classmethod
    def get_bloodbank(self,bloodbank):
        db=get_connection()
        cursor = db.cursor()

        get_query=f"SELECT * FROM BLOOD_BANK WHERE Bbank_id = '{bloodbank['Bbank_id']}'"
        try:
            cursor.execute(get_query)
            db.commit()
        except mysql.Error as err:
            print("Failed to fetch the blood bank details : {}".format(err))
            return {"status": 400, "entry": str(err)}
        db.close()
        return {"status":200,"entry": bloodbank}

    @classmethod
    def update_bloodbank(self,bloodbank):
        #update the phone no. of the bank
        if bloodbank["Bbank_id"] != None and bloodbank["Phone_no"] != None:
            db=get_connection()
            cursor = db.cursor()
            update_query = "UPDATE BLOOD_BANK set Phone_no=%s where Bbank_id =%s"
            try:
                cursor.execute(update_query,(bloodbank["Phone_no"],bloodbank["Bbank_id"]))
                db.commit()
                return {"status":201, "message":"Phone no updated Successfully"}
            except mysql.Error as err:
                print("Failed to update entry: {}".format(err))
                return {"status": 500, "message": str(err)}
            finally:
                db.close()
        
        if bloodbank["Bbank_id"] != None and bloodbank["Type"] != None:
            db=get_connection()
            cursor = db.cursor()
            update_query = "UPDATE BLOOD_BANK set Type=%s where Bbank_id =%s"
            try:
                cursor.execute(update_query,(bloodbank["Type"],bloodbank["Bbank_id"]))
                db.commit()
                return {"status":201, "message":"Bloodbank Type updated Successfully"}
            except mysql.Error as err:
                print("Failed to update entry: {}".format(err))
                return {"status": 500, "message": str(err)}
            finally:
                db.close()
        
        if bloodbank["Bbank_id"] != None and bloodbank["Name"] != None:
            db=get_connection()
            cursor = db.cursor()
            update_query = "UPDATE BLOOD_BANK set Name=%s where Bbank_id =%s"
            try:
                cursor.execute(update_query,(bloodbank["Name"],bloodbank["Bbank_id"]))
                db.commit()
                return {"status":201, "message":"Bloodbank Name updated Successfully"}
            except mysql.Error as err:
                print("Failed to update entry: {}".format(err))
                return {"status": 500, "message": str(err)}
            finally:
                db.close()

        

        

        


     