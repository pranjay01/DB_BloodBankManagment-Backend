#SJSU CMPE 138Spring2020 TEAM7

import mysql.connector as mysql
from connection import get_connection
from datetime import datetime
from security import authenticate
datetime.today().strftime('%Y-%m-%d')


class Operators:

    @classmethod
    def insert_operator(self, operator):
        db = get_connection()
        cursor = db.cursor()

        insert_query = "INSERT INTO OPERATOR (Operator_id,Name,Email,Password,Bbank_id)  VALUES (%s,%s,%s,%s,%s)"
        cursor.execute(insert_query, (operator['Operator_id'],operator['Name'], operator['Email'],
                                      operator['Password'],operator['Bbank_id']))

        db.commit()
        db.close()
        return "success"

    @classmethod
    def delete_operator(self, operator):
        db = get_connection()
        cursor = db.cursor()
        operator['Operator_id'] = int(operator['Operator_id'])
        
        delete_query = "DELETE FROM OPERATOR WHERE Operator_id =%s"
        try:
            cursor.execute(delete_query,(operator['Operator_id'],))
            db.commit()
            return {"status": 200, "entry": operator}

        except mysql.Error as err:
            print("Failed to delete entry: {}".format(err))
            return {"status": 400, "entry": str(err)}
        finally:
            db.close()

    @classmethod
    def get_operator(self):
        db = get_connection()
        cursor = db.cursor()

        get_query = "SELECT opr.Operator_id,opr.Name, opr.Email,opr.Bbank_id,bb.Name \
                    FROM OPERATOR as opr join BLOOD_BANK as bb on (bb.Bbank_id=opr.Bbank_id)"
        try:
            cursor.execute(get_query)
            result = cursor.fetchall()
            operator_list=[]
            for row in result:
                operator_list.append({"Operator_id":row[0], "Name":row[1],
                "Email":row[2], "Bbank_id":row[3],"Bbank_Name":row[4]})
            db.commit()
            return {"status": 200, "operator_list": operator_list}
        except mysql.Error as err:
            print("Failed to fetch the operator details : {}".format(err))
            return {"status": 400, "entry": str(err)}
        finally:
            db.close()

    @classmethod
    def update_operator_name(self,operator_entry,Operator_id):
        if int(Operator_id)==operator_entry["Operator_id"]:
            db=get_connection()
            cursor = db.cursor()
            update_query="update OPERATOR set Name=%s where Operator_id=%s"
            try:
                cursor.execute(update_query,(operator_entry["Name"],operator_entry["Operator_id"]))
                db.commit()
                return {"status":201, "message":"Operator details updated successfully"}
            except mysql.Error as err:
                print("Failed to update entry: {}".format(err))
                return {"status": 500, "message": str(err)}
            finally:
                db.close()
        else:
            return {"status": 401, "message": "Unauthorised Access"}

    @classmethod
    def update_operator_email(self,operator_entry,Operator_id):
        if int(Operator_id)==operator_entry["Operator_id"]:
            if authenticate(operator_entry["old_Email"],operator_entry["Password"]):
                db=get_connection()
                cursor = db.cursor()
                update_query="update OPERATOR set Email=%s where Operator_id=%s"
                try:
                    cursor.execute(update_query,(operator_entry["new_Email"],operator_entry["Operator_id"]))
                    db.commit()
                    return {"status":201, "message":"Operator's email-id updated successfully"}
                except mysql.Error as err:
                    print("Failed to update entry: {}".format(err))
                    return {"status": 500, "message": str(err)}
                finally:
                    db.close()
            else:
                return {"status": 401, "message": "Unauthorised Access"}
        else:
            return {"status": 401, "message": "Unauthorised Access"}


    @classmethod
    def update_operator_password(self,operator_entry,Operator_id):
        if int(Operator_id)==operator_entry["Operator_id"]:
            if authenticate(operator_entry["Email"],operator_entry["old_Password"]):
                db=get_connection()
                cursor = db.cursor()
                update_query="update OPERATOR set Password=%s where Operator_id=%s"
                try:
                    cursor.execute(update_query,(operator_entry["new_Password"],operator_entry["Operator_id"]))
                    db.commit()
                    return {"status":201, "message":"Operator's password updated successfully"}
                except mysql.Error as err:
                    print("Failed to update entry: {}".format(err))
                    return {"status": 500, "message": str(err)}
                finally:
                    db.close()
            else:
                return {"status": 401, "message": "Unauthorised Access"}
        else:
            return {"status": 401, "message": "Unauthorised Access"}



        # update the password of the operator
        # if operator["Operator_id"] != None and operator["Password"] != None:
        #     db = get_connection()
        #     cursor = db.cursor()
        #     update_query = "UPDATE OPERATOR set Password=%s where Operator_id =%s"
        #     try:
        #         cursor.execute(update_query, (operator["Password"], operator["Operator_id"]))
        #         db.commit()
        #         return {"status": 201, "message": "Password updated Successfully"}
        #     except mysql.Error as err:
        #         print("Failed to update entry: {}".format(err))
        #         return {"status": 500, "message": str(err)}
        #     finally:
        #         db.close()

        # # update the email_id of the operator
        # if operator["operator_id"] != None and operator["Email"] != None:
        #     db = get_connection()
        #     cursor = db.cursor()
        #     update_query = "UPDATE OPERATOR set Email=%s where Operator_id =%s"
        #     try:
        #         cursor.execute(update_query, (operator["Email"], operator["operator_id"]))
        #         db.commit()
        #         return {"status": 201, "message": "Operator Email updated Successfully"}
        #     except mysql.Error as err:
        #         print("Failed to update entry: {}".format(err))
        #         return {"status": 500, "message": str(err)}
        #     finally:
        #         db.close()

        # # update the name of the operator
        # if operator["Operator_id"] != None and operator["Name"] != None:
        #     db = get_connection()
        #     cursor = db.cursor()
        #     update_query = "UPDATE OPERATOR set Name=%s where operator_id =%s"
        #     try:
        #         cursor.execute(update_query, (operator["Name"], operator["Operator_id"]))
        #         db.commit()
        #         return {"status": 201, "message": "Operator Name updated Successfully"}
        #     except mysql.Error as err:
        #         print("Failed to update entry: {}".format(err))
        #         return {"status": 500, "message": str(err)}
        #     finally:
        #         db.close()

class Blood_donation_event:
    @classmethod
    def insert_blood_donation_event(self, blood_donation_event):
        db = get_connection()
        cursor = db.cursor()
        try:
            insert_query = "INSERT INTO BLOOD_DONATION_EVENT (Name,Date_of_event,Venue,Operator_id) VALUES (%s,%s,%s,%s)"
            cursor.execute(insert_query, (blood_donation_event['Name'],
                                        blood_donation_event['Date_of_event'], blood_donation_event['Venue'],
                                        blood_donation_event['Operator_id']))

            db.commit()
        except mysql.Error as err:
                print("Internal Server error: {}".format(err))
                return {"status": 500, "message": str(err)}

        finally:
            db.close()
        return {"status": 200, "event": blood_donation_event}

    # @classmethod
    # def delete_blood_donation_drive(self, blood_donation_event):
    #     db = get_connection()
    #     cursor = db.cursor()

    #     delete_query = f"DELETE FROM BLOOD_DONATION_EVENT WHERE DRIVE_id = '{blood_donation_event['Drive_id']}'"
    #     try:
    #         cursor.execute(delete_query)
    #         db.commit()
    #     except mysql.Error as err:
    #         print("Failed to delete entry: {}".format(err))
    #         return {"status": 400, "entry": str(err)}
    #     db.close()
    #     return {"status": 200, "entry": blood_donation_event}

    @classmethod
    def get_blood_donation_event(self, blood_donation_event):
        db = get_connection()
        cursor = db.cursor()

        get_query = f"SELECT Drive_id,Name,Date_of_event,\
        Venue,Operator_id FROM BLOOD_DONATION_EVENT WHERE Drive_id = {blood_donation_event['Drive_id']} \
                        AND Operator_id = {blood_donation_event['Operator_id']}"
        try:
            cursor.execute(get_query)
            result = cursor.fetchone()
            date=result[2].strftime('%Y-%m-%d')
            event = {"Drive_id":result[0],"Name":result[1],"Date_of_event":date
            ,"Venue":result[3],"Operator_id":result[4]}
            db.commit()
            return {"status": 200, "entry": event}
        except mysql.Error as err:
            print("Failed to fetch the blood donation event details : {}".format(err))
            return {"status": 400, "entry": str(err)}
        finally:
            db.close()
        


    @classmethod
    def get_operator_vent_list(self,operator_id):
        db = get_connection()
        cursor = db.cursor()

        get_query = f"SELECT * FROM BLOOD_DONATION_EVENT WHERE Operator_id = '{operator_id}'"
        try:
            cursor.execute(get_query)
            result = cursor.fetchall()
            event_list=[]
            for row in result:
                event_list.append({'Drive_id':row[0], 'Name':row[1],
                'Date_of_event':row[2], 'Venue':row[3]})
            return {"status": 200, "eventList": event_list}
        except mysql.Error as err:
            print("Failed to fetch the blood donation event details : {}".format(err))
            return {"status": 400, "entry": str(err)}
        finally:
            db.close()
        

    @classmethod
    def update_blood_donation_event(self, blood_donation_event):
        db=get_connection()
        cursor = db.cursor()
        if check_active(blood_donation_event["Drive_id"],blood_donation_event["Operator_id"],cursor):
            update_query = "UPDATE BLOOD_DONATION_EVENT set Name = %s, \
            Date_of_event=%s, Venue=%s where Drive_id=%s and Operator_id=%s"
            try:
                db=get_connection()
                cursor = db.cursor()
                cursor.execute(update_query,(blood_donation_event["Name"],blood_donation_event["Date_of_event"],
                blood_donation_event["Venue"],blood_donation_event["Drive_id"],blood_donation_event["Operator_id"]))
                db.commit()
                return {"status":201, "message":"Event updated succesfully"}
            except mysql.Error as err:
                print("Failed to update entry: {}".format(err))
                return {"status": 500, "message": str(err)}
            finally:
                db.close()
        else:
            return {"status":404, "message":"Event already expired, can't be updated"} 

    @classmethod
    def delete_blood_donation_event(self,event):
        event['Drive_id'] = int(event['Drive_id'])
        event['Operator_id'] = int(event['Operator_id'])
        db=get_connection()
        cursor = db.cursor()
        if check_active(event["Drive_id"],event["Operator_id"],cursor):
            select_query = "DELETE from BLOOD_DONATION_EVENT where Drive_id=%s \
                            and Operator_id=%s"
            try:
                cursor.execute(select_query,(event['Drive_id'],event['Operator_id']))
                db.commit()
                return {"status":200, "message":"event deleted succefully"}
            except mysql.Error as err:
                print("Failed to update entry: {}".format(err))
                return {"status": 500, "message": str(err)}
            finally:
                db.close()
        else:
            return {"status":404, "message":"Event already expired, can't be deleted"}

    @classmethod
    def get_active_event_list(self):
        db=get_connection()
        cursor = db.cursor()
        select_query="SELECT * FROM BLOOD_DONATION_EVENT WHERE Date_of_event>CURDATE() order by Date_of_event"
        try:
            cursor.execute(select_query)
            result = cursor.fetchall()
            events=[]
            for row in result:
                events.append({"Drive_id":row[0],"Name":row[1],
                "Date_of_event":row[2],"Venue":row[3]})
            db.commit()
            return {"status":200, "events":events}
        except mysql.Error as err:
            print("Failed to update entry: {}".format(err))
            return {"status": 500, "message": str(err)}
        finally:
            db.close()
    
        # update the Venue of the blood_donation_event
        # if blood_donation_event["Drive_id"] != None and blood_donation_event["Venue"] != None:
        #     db = get_connection()
        #     cursor = db.cursor()
        #     update_query = "UPDATE BLOOD_DONATION_EVENT set Venue=%s where Drive_id =%s"
        #     try:
        #         cursor.execute(update_query, (blood_donation_event["Venue"], blood_donation_event["Drive_id"]))
        #         db.commit()
        #         return {"status": 201, "message": "Blood donation event Venue updated Successfully"}
        #     except mysql.Error as err:
        #         print("Failed to update entry: {}".format(err))
        #         return {"status": 500, "message": str(err)}
        #     finally:
        #         db.close()

        # # update the Date of the Blood_donation_event
        # if blood_donation_event["Drive_id"] != None and blood_donation_event["Date_of_event"] != None:
        #     db = get_connection()
        #     cursor = db.cursor()
        #     update_query = "UPDATE BLOOD_DONATION_EVENT set Date_of_event=%s where Drive_id =%s"
        #     try:
        #         cursor.execute(update_query, (blood_donation_event["Date_of_event"], blood_donation_event["Drive_id"]))
        #         db.commit()
        #         return {"status": 201, "message": "Date of blood donation event updated Successfully"}
        #     except mysql.Error as err:
        #         print("Failed to update entry: {}".format(err))
        #         return {"status": 500, "message": str(err)}
        #     finally:
        #         db.close()

        # # update the name of the Blood donation event
        # if blood_donation_event["Drive_id"] != None and blood_donation_event["Name"] != None:
        #     db = get_connection()
        #     cursor = db.cursor()
        #     update_query = "UPDATE BLOOD_DONATION_EVENT set Name=%s where Drive_id =%s"
        #     try:
        #         cursor.execute(update_query, (blood_donation_event["Name"], blood_donation_event["Drive_id"]))
        #         db.commit()
        #         return {"status": 201, "message": " Name of blood donation event updated Successfully"}
        #     except mysql.Error as err:
        #         print("Failed to update entry: {}".format(err))
        #         return {"status": 500, "message": str(err)}
        #     finally:
        #             db.close()

def check_active(Drive_id,Operator_id,cursor):
    select_query = "SELECT Date_of_event from BLOOD_DONATION_EVENT where Drive_id=%s \
                        and Operator_id=%s"
    try:
        cursor.execute(select_query,(Drive_id,Operator_id))
        row = cursor.fetchone()
        if row:
            date= row[0]
            dateToday=datetime.today()
            if(date > dateToday):
                return True
            else:
                return False
        else:
            return{"status":200,"message":"Drive id doesn't belongs to operator"}
    except mysql.Error as err:
        print("Failed to update entry: {}".format(err))
        return {"status": 500, "message": str(err)}
   