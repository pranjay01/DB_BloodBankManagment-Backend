#SJSU CMPE 138Spring2020 TEAM7

import mysql.connector as mysql
from connection import get_connection
import base64


class Operator:
    def __init__(self,Operator_id,Name,Email,Password,Bbank_id):
        self.id =Operator_id
        self.Name =Name
        self.Email = Email
        self.Password =Password
        self.Bbank_id = Bbank_id

    @classmethod
    def find_by_email(self,email):
        db=get_connection()
        cursor = db.cursor()
        query = "SELECT * FROM OPERATOR WHERE Email=%s"
        try:
            cursor.execute(query,(email,))
            row = cursor.fetchone()
            if row:
                return self(*row)
            else:
                return None
        except mysql.Error as err:
            print("Internal Server error: {}".format(err))
            return {"status": 500, "message": str(err)}
        finally:
            db.close()

    @classmethod
    def find_by_id(self,_id):
        db=get_connection()
        cursor = db.cursor()
        query = "SELECT * FROM OPERATOR WHERE Operator_id=%s"
        try:
            cursor.execute(query,(_id,))
            row = cursor.fetchone()
            if row:
                return self(*row)
            else:
                return None
        except mysql.Error as err:
            print("Internal Server error: {}".format(err))
            return {"status": 500, "message": str(err)}
        finally:
            db.close()

    @classmethod
    def register(self,new_operator):
        db = get_connection()
        cursor = db.cursor()

        #data = request.get_json()
        query = "INSERT INTO OPERATOR VALUES (NULL,%s,%s,%s,%s)"
       # passwrd = new_operator['Password'].encode("ascii", "ignore")
        passwrd = base64.b64encode(new_operator['Password'].encode("utf-8"))
        try:
            cursor.execute(query,(new_operator['Name'], 
            new_operator['Email'],passwrd, new_operator['Bbank_id']))
            db.commit()
            return {"message": "Operator created successfully."}, 201
        except mysql.Error as err:
            print("Internal Server error: {}".format(err))
            return {"status": 500, "message": str(err)}
        finally:
            db.close()

    @classmethod
    def check_bankid(self,Operator_id,Bbank_id):
        Operator_id=int(Operator_id)
        oprator = self.find_by_id(Operator_id)
        if oprator and oprator.Bbank_id==Bbank_id:
            return True
        else:
            return None

    @classmethod
    def check_branch_id(self,Operator_id,branch_id):
        Operator_id=int(Operator_id)
        oprator = self.find_by_id(Operator_id)
        selectQuery = "Select Bbank_id FROM BRANCH WHERE Br_id=%s"
        db=get_connection()
        cursor = db.cursor()
        try:
            cursor.execute(selectQuery,(branch_id,))
            row = cursor.fetchone()
            if row and row[0]==oprator.Bbank_id:
                return True
            else:
                return None
        except mysql.Error as err:
            print("Internal Server error: {}".format(err))
            return {"status": 500, "message": str(err)}
        finally:
            db.close()

