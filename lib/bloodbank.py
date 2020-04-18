import mysql.connector as mysql
from connection import get_connection
from user import Operator

class Bloodbank:
    def __init__(self,Bbank_id,Name,Type,Phone_no):
        self.Bbank_id =Bbank_id
        self.Name =Name
        self.Type = Type
        self.Phone_no =Phone_no

    @classmethod
    def insert_bloodbank(self,bloodbank):
        db=get_connection()
        cursor = db.cursor()
        try:
            insert_query="INSERT INTO BLOOD_BANK (Name,Type,Phone_No)  VALUES (%s,%s,%s)"
            cursor.execute(insert_query,( bloodbank['Name'],bloodbank['Type'],bloodbank['Phone_No']))
            db.commit()
            return {"status":201, "message":"New Blood bank created"}
        except mysql.Error as err:
            return {"status": 500, "message": str(err)} 
        finally:
            db.close()

    @classmethod
    def delete_bloodbank(self,bloodbank):
        db=get_connection()
        cursor = db.cursor()

        delete_query="DELETE FROM BLOOD_BANK WHERE Bbank_id =%s"
        try:
            cursor.execute(delete_query,(bloodbank['Bbank_id'],))
            db.commit()
        except mysql.Error as err:
            print("Failed to delete entry: {}".format(err))
            return {"status": 400, "entry": str(err)}
        db.close()
        return {"status": 200, "message": "Blood Bank removed succesfully"}

    @classmethod
    def get_bloodbank(self,bloodbank):
        db=get_connection()
        cursor = db.cursor()
        # Get all the list f blood banks available and there info
        if bloodbank["case"] == 1:
            select_query="SELECT * FROM BLOOD_BANK"
            try:
                cursor.execute(select_query)
                result = cursor.fetchall()
                blood_banks=[]
                for row in result:
                    blood_banks.append(self(*row))
                    return {"status": 200, "result":blood_banks}
            except mysql.Error as err:
                print("Failed to fetch the blood bank details : {}".format(err))
                return {"status": 500, "message": str(err)}
            finally:
                db.close()
        #when information of only particular blood bank is required    
        elif bloodbank["case"] == 2:
            get_query="SELECT * FROM BLOOD_BANK WHERE Bbank_id = %s"
            try:
                cursor.execute(get_query,(bloodbank['Bbank_id'],))
                row = cursor.fetchone()
                return {"status": 200, "result":self(*row)}
            except mysql.Error as err:
                print("Failed to fetch the blood bank details : {}".format(err))
                return {"status": 500, "message": str(err)}
            db.close()
        else:
            return {"status": 404, "message": "Case not found"}

    @classmethod
    def update_bloodbank(self,bloodbank):
        db=get_connection()
        cursor = db.cursor()
        update_query = "UPDATE BLOOD_BANK set"
        args=[]
        for key in bloodbank:
            if bloodbank[key]:
                update_query = update_query + "set " + key + "=%s"
                args.append(bloodbank[key])
        try:
            argument = tuple(args)
            cursor.execute(update_query,argument)
            db.commit()
            return {"status":201, "message":"Bloodbank Name updated Successfully"}
        except mysql.Error as err:
            print("Failed to update entry: {}".format(err))
            return {"status": 500, "message": str(err)}
        finally:
            db.close()
        
        #update the phone no. of the bank
        # if bloodbank["Bbank_id"] != None and bloodbank["Phone_no"] != None:
        #     db=get_connection()
        #     cursor = db.cursor()
            

        #     update_query = "UPDATE BLOOD_BANK set Phone_no=%s where Bbank_id =%s"
        #     try:
        #         cursor.execute(update_query,(bloodbank["Phone_no"],bloodbank["Bbank_id"]))
        #         db.commit()
        #         return {"status":201, "message":"Phone no updated Successfully"}
        #     except mysql.Error as err:
        #         print("Failed to update entry: {}".format(err))
        #         return {"status": 500, "message": str(err)}
        #     finally:
        #         db.close()
        
        # # if bloodbank["Bbank_id"] != None and bloodbank["Type"] != None:
        # #     db=get_connection()
        # #     cursor = db.cursor()
        # #     update_query = "UPDATE BLOOD_BANK set Type=%s where Bbank_id =%s"
        # #     try:
        # #         cursor.execute(update_query,(bloodbank["Type"],bloodbank["Bbank_id"]))
        # #         db.commit()
        # #         return {"status":201, "message":"Bloodbank Type updated Successfully"}
        # #     except mysql.Error as err:
        # #         print("Failed to update entry: {}".format(err))
        # #         return {"status": 500, "message": str(err)}
        # #     finally:
        # #         db.close()
        
        # # if bloodbank["Bbank_id"] != None and bloodbank["Name"] != None:
        # #     db=get_connection()
        # #     cursor = db.cursor()
        # #     update_query = "UPDATE BLOOD_BANK set Name=%s where Bbank_id =%s"
        # #     try:
        # #         cursor.execute(update_query,(bloodbank["Name"],bloodbank["Bbank_id"]))
        # #         db.commit()
        # #         return {"status":201, "message":"Bloodbank Name updated Successfully"}
        # #     except mysql.Error as err:
        # #         print("Failed to update entry: {}".format(err))
        # #         return {"status": 500, "message": str(err)}
        # #     finally:
        # #         db.close()

class BloodBankBranch:
    def __init__(self,Br_id,Br_Type,Bbank_id,Street,City,Zip):
        self.Br_id =Br_id
        self.Br_Type =Br_Type
        self.Bbank_id = Bbank_id
        self.Street =Street
        self.City = City
        self.Zip =Zip

    @classmethod
    def creat_new_branch(self,branch,Operator_id):
        if Operator.check_bankid(Operator_id,branch["Bbank_id"]):       
            db=get_connection()
            cursor = db.cursor()
            try:
                insert_query="INSERT INTO BRANCH (Br_Type,Bbank_id,Street,City,Zip)  VALUES (%s,%s,%s,%s,%s)"
                cursor.execute(insert_query,( branch['Br_Type'],branch['Bbank_id'],branch['Street'],branch['City'],branch['Zip']))
                db.commit()
                return {"status":201, "message":"New branch created", "branch": branch}
            except mysql.Error as err:
                return {"status": 500, "message": str(err)} 
            finally:
                db.close()
        else:
            return {"status": 401, "message": "Unauthorised Access"}

    @classmethod
    def update_branch(self,branch,Operator_id):
        if Operator.check_branch_id(Operator_id,branch["Br_id"]):       
            db=get_connection()
            cursor = db.cursor()
            try:
                update_query="UPDATE BRANCH set Br_Type=%s, Street=%s, City=%s, Zip=%s where Br_id=%s"
                cursor.execute(update_query,( branch['Br_Type'],branch['Street'],branch['City'],branch['Zip'],branch['Br_id']))
                db.commit()
                return {"status":200, "message":"Branch updated"}
            except mysql.Error as err:
                return {"status": 500, "message": str(err)} 
            finally:
                db.close()
        else:
            return {"status": 401, "message": "Unauthorised Access"}
 
         
    @classmethod
    def delete_delete(self,branch,Operator_id):
        if Operator.check_branch_id(Operator_id,branch["Br_id"]):
            db=get_connection()
            cursor = db.cursor()
            try:
                delete_query="DELETE FROM BRANCH where Br_id=%s"
                cursor.execute(delete_query,(branch['Br_id']))
                db.commit()
                return {"status":200, "message":"Branch deleted successfully"}
            except mysql.Error as err:
                return {"status": 500, "message": str(err)} 
            finally:
                db.close()
        else:
            return {"status": 401, "message": "Unauthorised Access"}
       

        

        


     