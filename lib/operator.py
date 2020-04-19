import mysql.connector as mysql
from connection import get_connection
from datetime import datetime
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

        delete_query = f"DELETE FROM OPERATOR WHERE Operator_id = '{operator['Operator_id']}'"
        try:
            cursor.execute(delete_query)
            db.commit()
            return {"status": 200, "entry": operator}

        except mysql.Error as err:
            print("Failed to delete entry: {}".format(err))
            return {"status": 400, "entry": str(err)}
        finally:
            db.close()

    @classmethod
    def get_operator(self, operator):
        db = get_connection()
        cursor = db.cursor()

        get_query = "SELECT * FROM OPERATOR "
        try:
            cursor.execute(get_query)
            result = cursor.fetchall()
            operator_list=[]
            for row in result:
                operator_list.append({"Operator_id":row[0], "Name":row[1],
                "Email":row[2], "Bbank_id":row[4]})
            db.commit()
            return {"status": 200, "operator_list": operator_list}
        except mysql.Error as err:
            print("Failed to fetch the operator details : {}".format(err))
            return {"status": 400, "entry": str(err)}
        finally:
            db.close()

    @classmethod
    def update_operator(self, operator):
        db=get_connection()
        cursor = db.cursor()
        update_query = "UPDATE OPERATOR set"
        args=[]
        for key in operator:
            if operator[key]:
                update_query = update_query + "set " + key + "=%s"
                args.append(operator[key])
        try:
            argument = tuple(args)
            cursor.execute(update_query,argument)
            db.commit()
            return {"status":201, "message":"Operator details updated successfully"}
        except mysql.Error as err:
            print("Failed to update entry: {}".format(err))
            return {"status": 500, "message": str(err)}
        finally:
            db.close()



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

    @classmethod
    def delete_blood_donation_drive(self, blood_donation_event):
        db = get_connection()
        cursor = db.cursor()

        delete_query = f"DELETE FROM BLOOD_DONATION_EVENT WHERE DRIVE_id = '{blood_donation_event['Drive_id']}'"
        try:
            cursor.execute(delete_query)
            db.commit()
        except mysql.Error as err:
            print("Failed to delete entry: {}".format(err))
            return {"status": 400, "entry": str(err)}
        db.close()
        return {"status": 200, "entry": blood_donation_event}

    @classmethod
    def get_blood_donation_event(self, blood_donation_event):
        db = get_connection()
        cursor = db.cursor()

        get_query = f"SELECT * FROM BLOOD_DONATION_EVENT WHERE Drive_id = '{blood_donation_event['Drive_id']}' \
                        AND Operator_id = '{blood_donation_event['Operator_id']}'"
        try:
            cursor.execute(get_query)
            db.commit()
            return {"status": 200, "entry": blood_donation_event}
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
        

        select_query = "SELECT Date_of_event from BLOOD_DONATION_EVENT where Drive_id=%s \
                        and Operator_id=%s"
        try:
            db=get_connection()
            cursor = db.cursor()
            cursor.execute(select_query,(blood_donation_event['Drive_id'],blood_donation_event['Operator_id']))
            row = cursor.fetchone()
            date= row[0]
            dateToday=datetime.today().strftime('%Y-%m-%d')
            if(date < dateToday):
                return {"status":404, "message":"Event already expired, can't be updated"} 
        except mysql.Error as err:
            print("Failed to update entry: {}".format(err))
            return {"status": 500, "message": str(err)}
        finally:
            db.close()
        update_query = "UPDATE BLOOD_DONATION_EVENT set"
        args=[]
        for key in blood_donation_event:
            if blood_donation_event[key]:
                update_query = update_query + "set " + key + "=%s"
                args.append(blood_donation_event[key])
        try:
            db=get_connection()
            cursor = db.cursor()
            argument = tuple(args)
            cursor.execute(update_query,argument)
            db.commit()
            return {"status":201, "message":"Event updated succesfully"}
        except mysql.Error as err:
            print("Failed to update entry: {}".format(err))
            return {"status": 500, "message": str(err)}
        finally:
            db.close()


    @classmethod
    def delete_blood_donation_event(self,event):
        select_query = "DELETE from BLOOD_DONATION_EVENT where Drive_id=%s \
                        and Operator_id=%s"
        try:
            db=get_connection()
            cursor = db.cursor()
            cursor.execute(select_query,(event['Drive_id'],event['Operator_id']))
            db.commit()
            return {"status":200, "message":"event deleted succefully"}
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