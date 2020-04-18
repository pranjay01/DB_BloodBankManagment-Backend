import mysql.connector as mysql
from create_operator_table import get_connection


class Operator:

    @classmethod
    def insert_operator(self, operator):
        db = get_connection('root','excel2020')
        cursor = db.cursor()

        insert_query = "INSERT INTO OPERATOR (Operator_id,Name,Email,Password,Bbank_id)  VALUES (%s,%s,%s,%s,%s)"
        cursor.execute(insert_query, (operator['Operator_id'],operator['Name'], operator['Email'],
                                      operator['Password'],operator['Bbank_id']))

        db.commit()
        db.close()
        return "success"

    @classmethod
    def delete_operator(self, operator):
        db = get_connection('root','excel2020')
        cursor = db.cursor()

        delete_query = f"DELETE FROM OPERATOR WHERE Operator_id = '{operator['Operator_id']}'"
        try:
            cursor.execute(delete_query)
            db.commit()
        except mysql.Error as err:
            print("Failed to delete entry: {}".format(err))
            return {"status": 400, "entry": str(err)}
        db.close()
        return {"status": 200, "entry": operator}

    @classmethod
    def get_operator(self, operator):
        db = get_connection('root','excel2020')
        cursor = db.cursor()

        get_query = f"SELECT * FROM OPERATOR WHERE Operator_id = '{operator['operator_id']}'"
        try:
            cursor.execute(get_query)
            db.commit()
        except mysql.Error as err:
            print("Failed to fetch the operator details : {}".format(err))
            return {"status": 400, "entry": str(err)}
        db.close()
        return {"status": 200, "entry": operator}

    @classmethod
    def update_operator(self, operator):
        # update the password of the operator
        if operator["Operator_id"] != None and operator["Password"] != None:
            db = get_connection('root','excel2020')
            cursor = db.cursor()
            update_query = "UPDATE OPERATOR set Password=%s where Operator_id =%s"
            try:
                cursor.execute(update_query, (operator["Password"], operator["Operator_id"]))
                db.commit()
                return {"status": 201, "message": "Password updated Successfully"}
            except mysql.Error as err:
                print("Failed to update entry: {}".format(err))
                return {"status": 500, "message": str(err)}
            finally:
                db.close()

        # update the email_id of the operator
        if operator["operator_id"] != None and operator["Email"] != None:
            db = get_connection('root','excel2020')
            cursor = db.cursor()
            update_query = "UPDATE OPERATOR set Email=%s where Operator_id =%s"
            try:
                cursor.execute(update_query, (operator["Email"], operator["operator_id"]))
                db.commit()
                return {"status": 201, "message": "Operator Email updated Successfully"}
            except mysql.Error as err:
                print("Failed to update entry: {}".format(err))
                return {"status": 500, "message": str(err)}
            finally:
                db.close()

        # update the name of the operator
        if operator["Operator_id"] != None and operator["Name"] != None:
            db = get_connection('root','excel2020')
            cursor = db.cursor()
            update_query = "UPDATE OPERATOR set Name=%s where operator_id =%s"
            try:
                cursor.execute(update_query, (operator["Name"], operator["Operator_id"]))
                db.commit()
                return {"status": 201, "message": "Operator Name updated Successfully"}
            except mysql.Error as err:
                print("Failed to update entry: {}".format(err))
                return {"status": 500, "message": str(err)}
            finally:
                db.close()

 class Blood_donation_event:

                @classmethod
                def insert_blood_donation_event(self, blood_donation_event):
                    db = get_connection('root','excel2020')
                    cursor = db.cursor()

                    insert_query = "INSERT INTO BLOOD_DONATION_EVENT (Drive_id,Name,Date_of_event,Venue,Operator_id) VALUES (%s,%s,%s,%s,%s)"
                    cursor.execute(insert_query, (blood_donation_event['Drive_id'],blood_donation_event['Name'],
                                                  blood_donation_event['Date_of_event'], blood_donation_event['Venue'],
                                                  blood_donation_event['Operator_id']))

                    db.commit()
                    db.close()
                    return "success"

                @classmethod
                def delete_blood_donation_drive(self, blood_donation_drive):
                    db = get_connection('root','excel2020')
                    cursor = db.cursor()

                    delete_query = f"DELETE FROM BLOOD_DONATION_DRIVE WHERE DRIVE_id = '{blood_donation_event['Drive_id']}'"
                    try:
                        cursor.execute(delete_query)
                        db.commit()
                    except mysql.Error as err:
                        print("Failed to delete entry: {}".format(err))
                        return {"status": 400, "entry": str(err)}
                    db.close()
                    return {"status": 200, "entry": blood_donation_drive}

                @classmethod
                def get_blood_donation_event(self, blood_donation_event):
                    db = get_connection('root','excel2020')
                    cursor = db.cursor()

                    get_query = f"SELECT * FROM BLOOD_DONATION_EVENT WHERE Drive_id = '{blood_donation_event['Drive_id']}'"
                    try:
                        cursor.execute(get_query)
                        db.commit()
                    except mysql.Error as err:
                        print("Failed to fetch the blood donation event details : {}".format(err))
                        return {"status": 400, "entry": str(err)}
                    db.close()
                    return {"status": 200, "entry": blood_donation_event}

                @classmethod
                def update_blood_donation_event(self, blood_donation_event):
                    # update the Venue of the blood_donation_event
                    if blood_donation_event["Drive_id"] != None and blood_donation_event["Venue"] != None:
                        db = get_connection('root','excel2020')
                        cursor = db.cursor()
                        update_query = "UPDATE BLOOD_DONATION_EVENT set Venue=%s where Drive_id =%s"
                        try:
                            cursor.execute(update_query, (blood_donation_event["Venue"], blood_donation_event["Drive_id"]))
                            db.commit()
                            return {"status": 201, "message": "Blood donation event Venue updated Successfully"}
                        except mysql.Error as err:
                            print("Failed to update entry: {}".format(err))
                            return {"status": 500, "message": str(err)}
                        finally:
                            db.close()

                    # update the Date of the Blood_donation_event
                    if blood_donation_event["Drive_id"] != None and blood_donation_event["Date_of_event"] != None:
                        db = get_connection('root','excel2020')
                        cursor = db.cursor()
                        update_query = "UPDATE BLOOD_DONATION_EVENT set Date_of_event=%s where Drive_id =%s"
                        try:
                            cursor.execute(update_query, (blood_donation_event["Date_of_event"], blood_donation_event["Drive_id"]))
                            db.commit()
                            return {"status": 201, "message": "Date of blood donation event updated Successfully"}
                        except mysql.Error as err:
                            print("Failed to update entry: {}".format(err))
                            return {"status": 500, "message": str(err)}
                        finally:
                            db.close()

                    # update the name of the Blood donation event
                    if blood_donation_event["Drive_id"] != None and blood_donation_event["Name"] != None:
                        db = get_connection('root','excel2020')
                        cursor = db.cursor()
                        update_query = "UPDATE BLOOD_DONATION_EVENT set Name=%s where Drive_id =%s"
                        try:
                            cursor.execute(update_query, (blood_donation_event["Name"], blood_donation_event["Drive_id"]))
                            db.commit()
                            return {"status": 201, "message": " Name of blood donation event updated Successfully"}
                        except mysql.Error as err:
                            print("Failed to update entry: {}".format(err))
                            return {"status": 500, "message": str(err)}
                        finally:
                             db.close()