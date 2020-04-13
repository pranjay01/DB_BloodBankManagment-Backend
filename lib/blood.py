import mysql.connector as mysql
from create_table import get_connection
from datetime import datetime

datetime.today().strftime('%Y-%m-%d')


class Blood:

    #method to insert blood unit in blood table
    @classmethod
    def insert_blood(self,bloodUnit):
        db=get_connection()
        cursor = db.cursor()

        date=datetime.today().strftime('%Y-%m-%d')
        bloodGroup_query = "SELECT Blood_Group from DONOR WHERE Donor_id = %s"
        try:
            cursor.execute(bloodGroup_query,(bloodUnit["Donor_id"],))
            if cursor.rowcount == 0:
                return {"status":404, "entry":"Donor id not found"}
            else:
                bloodGroup = cursor.fetchone()
                insert_query="INSERT INTO BLOOD (Blood_Group,Br_id,Donor_id,Donation_Date, \
                              Special_Attributes)  VALUES (%s,%s,%s,%s,%s)"
                try:
                    cursor.execute(insert_query,(bloodGroup, \
                    bloodUnit["Br_id"], bloodUnit["Donor_id"],date,bloodUnit["Special_Attributes"]))
                    db.commit()

                    return {"status":201, "message":"Bloodunit saved Successfully"}
                except mysql.Error as err:
                    print("Failed to add entry: {}".format(err))
                    return {"status": 500, "entry": str(err)}
        except mysql.Error as err:
            print("Internal Server error: {}".format(err))
            return {"status": 500, "entry": str(err)}

        finally:
            db.close()
        return "success"

    #get list of bllod units on different conditions
    @classmethod
    def get_blood_units(self,parameters):
        db=get_connection()
        cursor = db.cursor()
        #return the list containing count of blood units in each branch of a particular bank
        if parameters["case"] == 1:
            try:
                cursor.callproc('branch_wise_stock',(parameters["Bbank_id"],))
                if cursor.rowcount == 0:
                    return {"status":404, "entry":"branch id or blood group wrong"}
                else:
                    result = cursor.fetchall()
                    return {"status": 200, "result":result}

            except mysql.Error as err:
                print("Internal Server error: {}".format(err))
                return {"get_blood_unitsstatus": 500, "entry": str(err)}

            finally:
                db.close()

        #return the list containing count of blood units of each blood group type in a particular branch
        elif parameters["case"] == 2:
            try:
                cursor.callproc('branch_stock',(parameters["Br_id"],))
                if cursor.rowcount == 0:
                    return {"status":404, "entry":"branch id wrong"}
                else:
                    result = cursor.fetchall()
                    return {"status": 200, "result":result}

            except mysql.Error as err:
                print("Internal Server error: {}".format(err))
                return {"status": 500, "entry": str(err)}

            finally:
                db.close()
        #return the list of blood units for a particular blood group in a particular branch of blood bank
        elif parameters["case"] == 3:
            select_query="SELECT Blood_id, Blood_Group, Donor_id, Donation_Date, Date_of_Expiry, Special_Attributes \
                          FROM BLOOD \
                          WHERE Br_id=%s AND Blood_Group=%s"
            try:
                cursor.execute(select_query,(parameters["Br_id"],parameters["Blood_Group"]))
                if cursor.rowcount == 0:
                    return {"status":404, "entry":"branch id or Blood_Group is wrong"}
                else:
                    result = cursor.fetchall()
                    return {"status": 200, "result":result}
            except mysql.Error as err:
                print("Internal Server error: {}".format(err))
                return {"status": 500, "entry": str(err)}

            finally:
                db.close()
        else:
            return {"status": 404, "message": "Case not found"}


    @classmethod
    def get_bloodunit_list_guest_user(self,parameters):
        #Return the list containing the count of blood units in each blood bank
        if parameters["case"] == 1:
            db=get_connection()
            cursor = db.cursor()
            try:
                cursor.callproc('bloodbank_wise_stock')
                if cursor.rowcount == 0:
                    return {"status":404, "entry":"branch id or blood group wrong"}
                else:
                    result = cursor.fetchall()
                    return {"status": 200, "result":result}

            except mysql.Error as err:
                print("Internal Server error: {}".format(err))
                return {"status": 500, "entry": str(err)}

            finally:
                db.close()

        #return the list containing count of blood units in each branch of a particular bank
        elif parameters["case"] == 2:
            new_parameter = parameters
            case = {"case":1}
            new_parameter.update(case)
            return self.get_blood_units(new_parameter)

        #return the list containing count of blood units of each blood group type in a particular branch
        elif parameters["case"] == 3:
            new_parameter = parameters
            case = {"case":2}
            new_parameter.update(case)
            return self.get_blood_units(new_parameter)
        else:
            return {"status": 404, "message": "Case not found"}

    @classmethod
    def upadate_blood_bank(self,parameters):
        #update the special attributes of a particular blood unit
        if parameters["case"] == 1:
            db=get_connection()
            cursor = db.cursor()
            update_query = "UPDATE BLOOD set Special_Attributes=%s where Blood_id=%s"
            try:
                cursor.execute(update_query,(parameters["Special_Attributes"],parameters["Blood_id"]))
                db.commit()
                return {"status":201, "message":"Bloodunit updated Successfully"}
            except mysql.Error as err:
                print("Failed to update entry: {}".format(err))
                return {"status": 500, "entry": str(err)}

        #Move asked quantity of particular blood group blood from 1 branch to other branch
        elif parameters["case"] == 2:
            db=get_connection()
            cursor = db.cursor()
            update_query="UPDATE BLOOD SET Br_id=%s WHERE Br_id=%s AND Blood_Group=%s AND Date_of_Expiry > CURDATE() LIMIT %s"
            try:
                cursor.execute(update_query,(parameters["from_branch"],parameters["to_branch"],parameters["Blood_Group"], parameters["count"]))
                db.commit()
                return {"status":201, "message":"Bloodunit updated Successfully"}            
            except mysql.Error as err:
                return {"status": 500, "entry": str(err)}
        else:
            return {"status": 404, "message": "Case not found"}
    @classmethod
    def delete_blood_unit(self,parameters):
        db=get_connection()
        cursor = db.cursor()
        delete_query="DELETE FROM BLOOD WHERE Blood_id=%s"
        try:
            cursor.execute(delete_query,(parameters["Blood_id"],))
            db.commit()
        except mysql.Error as err:
            print("Internal Server error: {}".format(err))
            return {"status": 500, "entry": str(err)}
        finally:
            db.close()

    @classmethod
    def get_expired_units(self,parameters):
        db=get_connection()
        cursor = db.cursor()
        select_query="SELECT * FROM BLOOD WHERE Date_of_Expiry < CURDATE() AND Br_id IN \
                    (SELECT Br_id FROM BRANCH WHERE Bbank_id=%s)"
        try:
            cursor.execute(select_query,(parameters["Bbank_id"],))
            result = cursor.fetchall()
            db.commit()
            return {"status": 200, "result":result}
        except mysql.Error as err:
            print("Internal Server error: {}".format(err))
            return {"status": 500, "entry": str(err)}
        finally:
            db.close()

    @classmethod
    def delete_expired_units(self,parameters):
        db=get_connection()
        cursor = db.cursor()
        select_query="DELETE FROM BLOOD WHERE Date_of_Expiry < CURDATE() AND Br_id IN \
                    (SELECT Br_id FROM BRANCH WHERE Bbank_id=%s)"
        try:
            cursor.execute(select_query,(parameters["Bbank_id"],))
            db.commit()
            return {"status":200, "message":"Expired units deleted successfully"}
        except mysql.Error as err:
            print("Internal Server error: {}".format(err))
            return {"status": 500, "entry": str(err)}
        finally:
            db.close()
        

class BloodStock:

    @classmethod
    def update_blood_stock_limit(self,parameters):
        db=get_connection()
        cursor = db.cursor()
        update_query="UPDATE BLOOD_STOCK SET Btype_Limits=%s WHERE Br_id=%s AND Blood_Group=%s"
        try:
            cursor.execute(update_query,(parameters["Btype_Limits"],parameters["Br_id"],parameters["Blood_Group"]))
            db.commit()
        except mysql.Error as err:
            print("Internal Server error: {}".format(err))
            return {"status": 500, "entry": str(err)}
        finally:
            db.close()

