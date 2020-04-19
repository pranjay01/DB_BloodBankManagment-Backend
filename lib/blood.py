import mysql.connector as mysql
from connection import get_connection
from datetime import datetime
from user import Operator

datetime.today().strftime('%Y-%m-%d')


class Blood:

    #method to insert blood unit in blood table
    @classmethod
    def insert_blood(self,bloodUnit,Operator_id):
        db=get_connection()
        cursor = db.cursor()
        if True: #Operator.check_branch_id(Operator_id,bloodUnit["Br_id"]):       
            date=datetime.today().strftime('%Y-%m-%d')
            bloodGroup_query = "SELECT Blood_Group from DONOR WHERE Donor_id = %s"
            try:
                cursor.execute(bloodGroup_query,(bloodUnit["Donor_id"],))
                if cursor.rowcount == 0:
                    return {"status":404, "message":"Donor id not found"}
                else:
                    bloodGroup = cursor.fetchone()
                    insert_query="INSERT INTO BLOOD (Blood_Group,Br_id,Donor_id,Donation_Date, \
                                Special_Attributes)  VALUES (%s,%s,%s,%s,%s)"
                    try:
                        cursor.execute(insert_query,(bloodGroup[0], \
                        bloodUnit["Br_id"], bloodUnit["Donor_id"],date,bloodUnit["Special_Attributes"]))
                        db.commit()

                        return {"status":201, "message":"Bloodunit saved Successfully"}
                    except mysql.Error as err:
                        #print("Failed to add entry: {}".format(err))
                        return {"status": 500, "message": str(err)}
            except mysql.Error as err:
                print("Internal Server error: {}".format(err))
                return {"status": 500, "message": str(err)}

            finally:
                db.close()
            return "success"
        else:
            return {"status": 401, "message": "Unauthorised Access"}

    #get list of bllod units on different conditions
    @classmethod
    def get_blood_units(self,parameters,Operator_id):
        db=get_connection()
        cursor = db.cursor()
        #return the total count of bolood in the blood bank
        parameters["case"]=int(parameters["case"])
        # tmp = {"case":int(parameters["case"])}
        # parameters.update(tmp)

        if parameters["case"] == 4:
            parameters["Bbank_id"] = int(parameters["Bbank_id"])
            if True :#Operator.check_bankid(Operator_id,parameters["Bbank_id"]):
                try:
                    cursor.callproc('particular_bloodbank_stock',(parameters["Bbank_id"],))
                    if cursor.rowcount == 0:
                        return {"status":404, "message":"branch id or blood group wrong"}
                    else:
                        row = cursor.fetchone()
                        blood_bank = {'Blood_Bank_Name':row[1], 'Blood_Unit_Count':row[2]}
                        return {"status": 200, "result":blood_bank}

                except mysql.Error as err:
                    print("Internal Server error: {}".format(err))
                    return {"get_blood_unitsstatus": 500, "message": str(err)}

                finally:
                    db.close()
            else:
                return {"status": 401, "message": "Unauthorised Access"}
        #return the list containing count of blood units in each branch of a particular bank

        elif parameters["case"] == 1:
            parameters["Bbank_id"] = int(parameters["Bbank_id"])
            if True: #Operator.check_bankid(Operator_id,parameters["Bbank_id"]):
                try:
                    cursor.callproc('branch_wise_stock',(parameters["Bbank_id"],))
                    if cursor.rowcount == 0:
                        return {"status":404, "message":"branch id or blood group wrong"}
                    else:
                        result = cursor.fetchall()
                        blood_count=[]
                        for row in result:
                            blood_count.append({'Br_id':row[0], 'Br_Type':row[1], 'Blood_Unit_Count':row[2]})

                        return {"status": 200, "result":blood_count}

                except mysql.Error as err:
                    print("Internal Server error: {}".format(err))
                    return {"get_blood_unitsstatus": 500, "message": str(err)}

                finally:
                    db.close()
            else:
                return {"status": 401, "message": "Unauthorised Access"}
        #return the list containing count of blood units of each blood group type in a particular branch
        elif parameters["case"] == 2:
            parameters["Br_id"] = int(parameters["Br_id"])
            if True: #Operator.check_branch_id(Operator_id,parameters["Br_id"]):   
                try:
                    cursor.callproc('branch_stock',(parameters["Br_id"],))
                    if cursor.rowcount == 0:
                        return {"status":404, "message":"branch id wrong"}
                    else:
                        result = cursor.fetchall()
                        blood_count=[]
                        for row in result:
                            blood_count.append({'Blood_Group':row[0], 'Blood_Unit_Count':row[1]})

                        return {"status": 200, "result":blood_count}

                except mysql.Error as err:
                    print("Internal Server error: {}".format(err))
                    return {"status": 500, "message": str(err)}

                finally:
                    db.close()
            else:
                return {"status": 401, "message": "Unauthorised Access"}
        #return the list of blood units for a particular blood group in a particular branch of blood bank
        elif parameters["case"] == 3:
            parameters["Br_id"] = int(parameters["Br_id"])
            if True: #Operator.check_branch_id(Operator_id,parameters["Br_id"]):

                select_query="SELECT Blood_id, Blood_Group, Donor_id, Donation_Date, Date_of_Expiry, Special_Attributes \
                            FROM BLOOD \
                            WHERE Br_id=%s AND Blood_Group=%s"
                try:
                    cursor.execute(select_query,(parameters["Br_id"],parameters["Blood_Group"]))
                    if cursor.rowcount == 0:
                        return {"status":404, "message":"branch id or Blood_Group is wrong"}
                    else:
                        result = cursor.fetchall()
                        blood_units=[]
                        for row in result:
                            blood_units.append({'Blood_id':row[0], 'Blood_Group':row[1],
                                                'Donor_id':row[2],'Donation_Date':row[3],
                                                'Date_of_Expiry':row[4],'Special_Attributes':row[5],})

                        return {"status": 200, "result":blood_units}
                except mysql.Error as err:
                    print("Internal Server error: {}".format(err))
                    return {"status": 500, "message": str(err)}

                finally:
                    db.close()
            else:
                return {"status": 401, "message": "Unauthorised Access"}
        else:
            return {"status": 404, "message": "Case not found"}


    @classmethod
    def get_bloodunit_list_guest_user(self,parameters):
        #Return the list containing the count of blood units in each blood bank
        parameters["case"]=int(parameters["case"])
        if parameters["case"] == 1:
            db=get_connection()
            cursor = db.cursor()
            try:
                cursor.callproc('bloodbank_wise_stock')
                if cursor.rowcount == 0:
                    return {"status":404, "message":"branch id or blood group wrong"}
                else:
                    result = cursor.fetchall()
                    blood_count=[]
                    for row in result:
                        blood_count.append({'Bbank_id':row[0], 'Blood_Bank_Name':row[1], 'Blood_Unit_Count':row[2]})

                    return {"status": 200, "result":blood_count}
            except mysql.Error as err:
                print("Internal Server error: {}".format(err))
                return {"status": 500, "message": str(err)}

            finally:
                db.close()

        #return the list containing count of blood units in each branch of a particular bank
        elif parameters["case"] == 2:
            parameters["Bbank_id"]=int(parameters["Bbank_id"])
            try:
                cursor.callproc('branch_wise_stock',(parameters["Bbank_id"],))
                if cursor.rowcount == 0:
                    return {"status":404, "message":"branch id or blood group wrong"}
                else:
                    result = cursor.fetchall()
                    blood_count=[]
                    for row in result:
                        blood_count.append({'Br_id':row[0], 'Br_Type':row[1], 'Blood_Unit_Count':row[2]})
                    return {"status": 200, "result":blood_count}
            except mysql.Error as err:
                print("Internal Server error: {}".format(err))
                return {"get_blood_unitsstatus": 500, "message": str(err)}

            finally:
                db.close()

        #return the list containing count of blood units of each blood group type in a particular branch
        elif parameters["case"] == 3:
            parameters["Br_id"]=int(parameters["Br_id"])
            try:
                cursor.callproc('branch_stock',(parameters["Br_id"],))
                if cursor.rowcount == 0:
                    return {"status":404, "message":"branch id wrong"}
                else:
                    result = cursor.fetchall()
                    blood_count=[]
                    for row in result:
                        blood_count.append({'Blood_Group':row[0], 'Blood_Unit_Count':row[1]})

                    return {"status": 200, "result":blood_count}

            except mysql.Error as err:
                print("Internal Server error: {}".format(err))
                return {"status": 500, "message": str(err)}

            finally:
                db.close()
        else:
            return {"status": 404, "message": "Case not found"}

    @classmethod
    def upadate_blood_bank(self,parameters,Operator_id):              
            #update the special attributes of a particular blood unit
        if parameters["case"] == 1:
            if True: #Operator.check_branch_id(Operator_id,parameters["Br_id"]):       
                db=get_connection()
                cursor = db.cursor()
                update_query = "UPDATE BLOOD set Special_Attributes=%s where Blood_id=%s"
                try:
                    cursor.execute(update_query,(parameters["Special_Attributes"],parameters["Blood_id"]))
                    db.commit()
                    return {"status":201, "message":"Bloodunit updated Successfully"}
                except mysql.Error as err:
                    print("Failed to update entry: {}".format(err))
                    return {"status": 500, "message": str(err)}
                finally:
                    db.close()
            else:
                return {"status": 401, "message": "Unauthorised Access"}
    #Move asked quantity of particular blood group blood from 1 branch to other branch
        elif parameters["case"] == 2:
            #source = Operator.check_branch_id(Operator_id,parameters["from_branch"])
            #target = Operator.check_branch_id(Operator_id,parameters["to_branch"])
            #if  source and target :
            if  True and True :           
                db=get_connection()
                cursor = db.cursor()
                update_query="UPDATE BLOOD SET Br_id=%s WHERE Br_id=%s AND Blood_Group=%s AND Date_of_Expiry > CURDATE() LIMIT %s"
                try:
                    cursor.execute(update_query,(parameters["from_branch"],parameters["to_branch"],parameters["Blood_Group"], parameters["Count"]))
                    db.commit()
                    return {"status":201, "message":"Bloodunit updated Successfully"}            
                except mysql.Error as err:
                    return {"status": 500, "message": str(err)}
            else:
                return {"status": 401, "message": "Unauthorised Access"}
        else:
            return {"status": 404, "message": "Case not found"}
    @classmethod
    def delete_blood_unit(self,parameters,Operator_id):
        if True: #Operator.check_branch_id(Operator_id,parameters["Br_id"]):
                
            db=get_connection()
            cursor = db.cursor()
            delete_query="DELETE FROM BLOOD WHERE Blood_id=%s"
            try:
                cursor.execute(delete_query,(parameters["Blood_id"],))
                db.commit()
                return {"status": 200, "message":"Blood unit deleted successfully"}
            except mysql.Error as err:
                print("Internal Server error: {}".format(err))
                return {"status": 500, "message": str(err)}
            finally:
                db.close()
        else:
                return {"status": 401, "message": "Unauthorised Access"}


    @classmethod
    def get_expired_units(self,parameters,Operator_id):
        if True: #Operator.check_bankid(Operator_id,parameters["Bbank_id"]):   
            db=get_connection()
            cursor = db.cursor()
            select_query="SELECT * FROM BLOOD WHERE Date_of_Expiry < CURDATE() AND Br_id IN \
                        (SELECT Br_id FROM BRANCH WHERE Bbank_id=%s)"
            try:
                cursor.execute(select_query,(parameters["Bbank_id"],))
                result = cursor.fetchall()
                blood_units=[]
                db.commit()
                for row in result:
                    blood_units.append({'Blood_id':row[0], 'Blood_Group':row[2],
                                        'Br_id': row[3],'Special_Attributes':row[1],
                                        'Donor_id':row[4],'Donation_Date':row[5],
                                        'Date_of_Expiry':row[6]})

                return {"status": 200, "result":blood_units}
            except mysql.Error as err:
                print("Internal Server error: {}".format(err))
                return {"status": 500, "message": str(err)}
            finally:
                db.close()
        else:
            return {"status": 401, "message": "Unauthorised Access"}

    @classmethod
    def delete_expired_units(self,parameters,Operator_id):
        if True: #Operator.check_bankid(Operator_id,parameters["Bbank_id"]):   
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
                return {"status": 500, "message": str(err)}
            finally:
                db.close()
        else:
            return {"status": 401, "message": "Unauthorised Access"}

class BloodStock:

    @classmethod
    def update_blood_stock_limit(self,parameters,Operator_id):
        if Operator.check_branch_id(Operator_id,parameters["Br_id"]):   
            db=get_connection()
            cursor = db.cursor()
            update_query="UPDATE BLOOD_STOCK SET Btype_Limits=%s WHERE Br_id=%s AND Blood_Group=%s"
            try:
                cursor.execute(update_query,(parameters["Btype_Limits"],parameters["Br_id"],parameters["Blood_Group"]))
                db.commit()
                return {"status":201, "message":"Bloodunit updated Successfully"}

            except mysql.Error as err:
                print("Internal Server error: {}".format(err))
                return {"status": 500, "message": str(err)}
            finally:
                db.close()
        else:
            return {"status": 401, "message": "Unauthorised Access"}
