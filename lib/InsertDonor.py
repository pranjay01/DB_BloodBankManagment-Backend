#SJSU CMPE 138Spring2020 TEAM7

import mysql.connector as mysql
from connection import get_connection
from user import Operator


class InsertInTable:

    @classmethod
    def donor(self, single_donor):
        # This method will update all Donor and donor contact related tables including
        # DONOR DONOR_EMAIL DONOR_PHONE AFFILIATED
        db = get_connection()
        cursor = db.cursor()
        branch_id=int(single_donor["Br_id"])
        if Operator.check_branch_id(single_donor["Operator_id"], branch_id):

            insert_query = """INSERT INTO DONOR
            (Donor_id,Name,Blood_group,Street,City,Zip,Paid_Unpaid,Notification_Subscription,Notification_Type,Operator_id)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            t = (None, single_donor['Name'], int(single_donor['Blood_Group']),
                 single_donor['Street'], single_donor['City'], single_donor['Zip'], single_donor['Paid_Unpaid'],
                 single_donor['Notification_Subscription'], single_donor['Notification_Type'], int(single_donor['Operator_id']))

            try:
                cursor.execute(insert_query, t)
                new_donor_id=cursor.lastrowid
                db.commit()

                # Last Donor ID is assumed to be the MAX()
                # LAST_INSERT_ID() is not working with multiple connnects
            except mysql.Error as err:
                print("Failed to add donor entry: {}".format(err))
                return {"status": 500, "message": str(err)}

            # Need to update this based on what Salman is expecting
            t = tuple(single_donor['Emails'].values())
            insert_query = "INSERT INTO DONOR_EMAIL (Donor_id,Email_id)  VALUES (%s,%s)"
            for x in t:
                try:
                    cursor.execute(insert_query, (new_donor_id, x))
                    db.commit()
                except mysql.Error as err:
                    print("Failed to add donor email entry: {}".format(err))
                    return {"status": 500, "message": str(err)}

            # Need to update this based on what Salman is expecting
            # Mulitple phones updated assuming all infromation is present in a nested
            t = tuple(single_donor['Phones'].values())
            insert_query = "INSERT INTO DONOR_PHONE (Donor_id,Phone_no)  VALUES (%s,%s)"
            for x in t:
                try:
                    cursor.execute(insert_query, (new_donor_id, x))
                    db.commit()
                except mysql.Error as err:
                    print("Failed to add donor phone entry: {}".format(err))
                    return {"status": 500, "message": str(err)}

            # Affiiate table entry is inserted directly when a new donor is added
            t = (new_donor_id, single_donor['Br_id'])
            insert_query = "INSERT INTO AFFILIATED (Donor_id,Br_id)  VALUES (%s,%s)"
            try:
                cursor.execute(insert_query, t)
                db.commit()
            except mysql.Error as err:
                print("Failed to add affiliated entry: {}".format(err))
                return {"status": 500, "message": str(err)}

            db.close()
            print("Donor added successfully")
            return {"status": 201, "message": "Success"}
        else:
            print("Unauthorised Access")
            return {"status": 401, "message": "Unauthorised Access"}

    @classmethod
    def donor_contact(self, single_donor):
        db = get_connection()
        cursor = db.cursor()

        # Remove the single contact field if single_donor json directly sends E contact info
        # single_contact = single_donor['EMERGENCY_CONTACT']
        if Operator.check_bankid(single_donor["Operator_id"], int(single_donor["Bbank_id"])):
            insert_query = "INSERT INTO EMERGENCY_CONTACT_INFO (Phone_no,Donor_id,Name)  VALUES (%s,%s,%s)"
            t = (int(single_donor['Phone_no']),
                 int(single_donor['Donor_id']), single_donor['Name'])
            try:
                cursor.execute(insert_query, t)
                db.commit()
            except mysql.Error as err:
                print("Failed to add donor contact entry: {}".format(err))
                return {"status": 500, "message": str(err)}

            # Need to update this based on what Salman is expecting

            t = tuple(single_donor['Emails'].values())
            insert_query = "INSERT INTO EMERGENCY_CONTACT_EMAIL (Phone_no,Donor_id,Email_id)  VALUES (%s,%s,%s)"
            for x in t:
                try:
                    cursor.execute(
                        insert_query, (int(single_donor['Phone_no']), int(single_donor['Donor_id']), x))
                    db.commit()
                except mysql.Error as err:
                    print("Failed to add contact phones entry: {}".format(err))
                    return {"status": 500, "message": str(err)}

            db.close()
            return {"status": 201, "message": "Success"}
        else:
            return {"status": 401, "message": "Unauthorised Access"}


class UpdateInTable:

    @classmethod
    def donor(self, single_donor):
        db = get_connection()
        cursor = db.cursor()
        if Operator.check_branch_id(single_donor["Operator_id"], single_donor["Br_id"]):
            update_query = """UPDATE DONOR SET Name = %s,
            Blood_group = %s,Street =%s,City= %s,Zip = %s,Paid_Unpaid =%s,
            Notification_Subscription = %s,Notification_Type = %s WHERE Donor_id =%s ;"""
            t = (single_donor['Name'], single_donor['Blood_group'],
                 single_donor['Street'], single_donor['City'], single_donor['Zip'], single_donor['Paid_Unpaid'],
                 single_donor['Notification_Subscription'], single_donor['Notification_Type'], single_donor['Donor_id'])
            try:
                cursor.execute(update_query, t)
                db.commit()
            except mysql.Error as err:
                print("Failed to add donor contact entry: {}".format(err))
                return {"status": 500, "message": str(err)}

            # Need to update this based on what Salman is expecting
            t = tuple(single_donor['Emails'].values())
            try:
                delete_query = f"DELETE FROM DONOR_EMAIL WHERE Donor_id = '{single_donor['Donor_id']}'"
                cursor.execute(delete_query)
                db.commit()
                insert_query = "INSERT INTO DONOR_EMAIL (Donor_id,Email_id)  VALUES (%s,%s)"
                for x in t:
                    cursor.execute(insert_query, (single_donor['Donor_id'], x))
                    db.commit()
            except mysql.Error as err:
                print("Failed to update donor email entry: {}".format(err))
                return {"status": 500, "message": str(err)}

            # Need to update this based on what Salman is expecting
            t = tuple(single_donor['Phones'].values())
            try:
                delete_query = f"DELETE FROM DONOR_PHONE WHERE Donor_id = '{single_donor['Donor_id']}'"
                cursor.execute(delete_query)
                db.commit()
                insert_query = "INSERT INTO DONOR_PHONE (Donor_id,Phone_no)  VALUES (%s,%s)"
                for x in t:
                    cursor.execute(insert_query, (single_donor['Donor_id'], x))
                    db.commit()
            except mysql.Error as err:
                print("Failed to update donor email entry: {}".format(err))
                return {"status": 500, "message": str(err)}

            db.close()
            return {"status": 201, "message": "Success"}
        else:
            return {"status": 401, "message": "Unauthorised Access"}

    @classmethod
    def donor_contact(self, single_donor):
        db = get_connection()
        cursor = db.cursor()

        if Operator.check_bankid(single_donor["Operator_id"], single_donor["Bbank_id"]):
            update_query = """UPDATE EMERGENCY_CONTACT_INFO SET Name = %s WHERE Donor_id =%s 
            AND Phone_no=%s;"""
            t = (single_donor['Name'], int(single_donor['Donor_id']),int(single_donor['Phone_no']))
            try:
                cursor.execute(update_query, t)
                db.commit()
            except mysql.Error as err:
                print("Failed to update donor contact entry: {}".format(err))
                return {"status": 500, "message": str(err)}

            # Need to update this based on what Salman is expecting
            t = tuple(single_donor['Emails'].values())
            try:
                delete_query = f"DELETE FROM EMERGENCY_CONTACT_EMAIL WHERE \
                    Donor_id = {int(single_donor['Donor_id'])} and Phone_no={int(single_donor['Phone_no'])}"
                cursor.execute(delete_query)
                db.commit()
                insert_query = "INSERT INTO EMERGENCY_CONTACT_EMAIL (Phone_no,Donor_id,Email_id)  VALUES (%s,%s,%s)"
                for x in t:
                    cursor.execute(
                        insert_query, (int(single_donor['Phone_no']), int(single_donor['Donor_id']), x))
                    db.commit()
            except mysql.Error as err:
                print("Failed to update donor comtact email entry: {}".format(err))
                return {"status": 500, "message": str(err)}

            db.close()
            return {"status": 201, "message": "Success"}
        else:
            return {"status": 401, "message": "Unauthorised Access"}


class DeleteInTable:

    @classmethod
    def donor(self, single_donor):
        # Member function only deletes donor from the DONOR table
        # Delete on cascade expected to take care of the rest
        bank_id=int(single_donor["Bbank_id"])
        db = get_connection()
        cursor = db.cursor()
        if Operator.check_bankid(single_donor["Operator_id"], bank_id):
            delete_query = f"DELETE FROM DONOR WHERE Donor_id = {int(single_donor['Donor_id'])} "
            try:
                cursor.execute(delete_query)
                db.commit()
            except mysql.Error as err:
                print("Failed to delete entry: {}".format(err))
                return {"status": 500, "message": str(err)}
            db.close()
            return {"status": 200, "message": "Success"}
        else:
            return {"status": 401, "message": "Unauthorised Access"}

    @classmethod
    def donor_contact(self, single_donor):
        # Member function only to delete ONE donor contact from the DONOR_CONTACT table
        db = get_connection()
        cursor = db.cursor()
        try:
            cursor.execute(f"""SELECT * FROM EMERGENCY_CONTACT_INFO
                WHERE Donor_id = '{single_donor['Donor_id']}'""")
            t = cursor.fetchall()
            if (len(t) > 1):
                delete_query = f"""DELETE FROM EMERGENCY_CONTACT_INFO
                WHERE Donor_id = '{single_donor['Donor_id']}'
                AND Phone_no = '{single_donor['Phone_no']}'"""
                try:
                    cursor.execute(delete_query)
                    db.commit()
                except mysql.Error as err:
                    print("Failed to delete entry: {}".format(err))
                    return {"status": 500, "message": str(err)}
            else:
                s = "Each Donor requires at least one Donor.Delete Fail"
                print(s)
                return {"status": 500, "message": s}
        except mysql.Error as err:
            print("Failed to get donor contact data: {}".format(err))
            return {"status": 500, "message": str(err)}

        db.close()
        return {"status": 200, "message": "Success"}
    
class SelectInTable:

    @classmethod
    def donor(self, single_donor):
        # Selects and returns data from all donor related tables
        # mulitple select statements exceuted instead of a join since all data is passed in nested fashion
        db = get_connection()
        cursor = db.cursor()

        try:
            cursor.execute(
                f"""SELECT * FROM DONOR d JOIN DONOR_EMAIL e ON d.Donor_id = e.Donor_id
                WHERE Email_id = '{single_donor['Email_id']}'""")
            t = cursor.fetchone()
            if not t:
                return {"status": 500, "message": "No donor found with given email-id"}
            else:

                mydonor = {'Donor_id': t[0], 'Name': t[1], 'Blood_group': t[2],
                        'Street': t[3], 'City': t[4], 'Zip': t[5], 'Paid_Unpaid': t[6],
                        'Notification_Subscription': t[7], 'Notification_Type': t[8],
                        'Operator_id': t[9]}
                var_donor = t[0]
        except mysql.Error as err:
            print("Failed to get donor data: {}".format(err))
            return {"status": 500, "message": str(err)}

        try:
            cursor.execute(
                f"SELECT * FROM DONOR_EMAIL WHERE Donor_id = '{var_donor}'")
            t = cursor.fetchall()
            i = 0
            mydemail = {}
            for row in t:
                mydemail.update({f'Email{i}': row[1]})
                i = i+1
            mydonor["Emails"] = mydemail
        except mysql.Error as err:
            print("Failed to get donor emails: {}".format(err))
            return {"status": 500, "message": str(err)}

        try:
            cursor.execute(
                f"SELECT * FROM DONOR_PHONE WHERE Donor_id = '{var_donor}'")
            t = cursor.fetchall()
            i = 0
            mydphone = {}
            for row in t:
                mydphone.update({f'Phone{i}': row[0]})
                i = i+1
            mydonor["Phones"] = mydphone
        except mysql.Error as err:
            print("Failed to get donor Phones: {}".format(err))
            return {"status": 500, "message": str(err)}

        try:
            cursor.execute(
                f"SELECT Br_id FROM AFFILIATED WHERE Donor_id = '{var_donor}'")
            row=cursor.fetchone()
            mydonor['Br_id'] = row[0]
        except mysql.Error as err:
            print("Failed to get donor data: {}".format(err))
            return {"status": 500, "message": str(err)}

        db.close()
        return {"status": 200, "message": mydonor}

    @classmethod
    def get_donor_emergency_contact(self, single_donor):
        db = get_connection()
        cursor = db.cursor()
        try:
            select_query = "select * from EMERGENCY_CONTACT_INFO where Donor_id=%s"
            cursor.execute(select_query,(int(single_donor["Donor_id"]),))
            result = cursor.fetchall()
            contact_list=[]
            if result:
                for row in result:
                    contact_list.append({"Donor_id":row[1],"Name":row[2],"Phone_no":row[0]})
                return {"status":200, "contact_list":contact_list}
            else:
                return {"status":200, "contact_list":contact_list}
        except mysql.Error as err:
            print("Failed to get donor data: {}".format(err))
            return {"status": 500, "message": str(err)}
        finally:
            db.close()

    @classmethod
    def get_complete_econtact_info(self, single_donor):
        db = get_connection()
        cursor = db.cursor()
        try:
            select_query = "select * from EMERGENCY_CONTACT_INFO \
                where Donor_id=%s AND Phone_no=%s"
            cursor.execute(select_query,(int(single_donor["Donor_id"]),int(single_donor["Phone_no"])))
            result = cursor.fetchone()
            contact_info={}
            if result:
                contact_info = {"Donor_id":result[1],"Name":result[2],"Phone_no":result[0]}
            else:
                return {"status":200, "contact_info":contact_info}

            select_query = "select * from EMERGENCY_CONTACT_EMAIL \
                where Donor_id=%s AND Phone_no=%s"
            cursor.execute(select_query,(int(single_donor["Donor_id"]),int(single_donor["Phone_no"])))

            result = cursor.fetchall()
            email_list={}
            i=1
            if result:
                for row in result:
                    tmp = {f"Email-{i}":row[2]}
                    email_list.update(tmp)
                    i+=1
                tmp = {"Email_id":email_list}
                contact_info.update(tmp)
                return {"status":200, "contact_list":contact_info}
            else:
                return {"status":200, "contact_list":contact_info}
            
        except mysql.Error as err:
            print("Failed to get donor data: {}".format(err))
            return {"status": 500, "message": str(err)}
        finally:
            db.close()


    @classmethod
    def donor_contact(self, single_donor):
        # Selects and returns data for single contact from all donor contact related tables
        # Mulitple select statements exceuted instead of a join since all data is passed in nested fashion
        db = get_connection()
        cursor = db.cursor()

        try:
            cursor.execute(
                f"""SELECT * FROM EMERGENCY_CONTACT_INFO
                WHERE Donor_id = '{single_donor['Donor_id']}'
                AND Phone_no = '{single_donor['Phone_no']}'""")
            t = cursor.fetchone()
            mydonor = {'Phone_no': t[0], 'Donor_id': t[1], 'Name': t[2]}
        except mysql.Error as err:
            print("Failed to get donor contact data: {}".format(err))
            return {"status": 500, "message": str(err)}

        try:
            cursor.execute(
                f"""SELECT * FROM EMERGENCY_CONTACT_EMAIL
                WHERE Donor_id = '{single_donor['Donor_id']}'
                AND Phone_no = '{single_donor['Phone_no']}'""")
            t = cursor.fetchall()
            i = 0
            mydemail = {}
            for row in t:
                mydemail.update({f'Email{i}': row[2]})
                i = i+1
            mydonor["Emails"] = mydemail
        except mysql.Error as err:
            print("Failed to get donor emails: {}".format(err))
            return {"status": 500, "message": str(err)}

        db.close()
        return {"status": 200, "message": mydonor}

    @classmethod
    def donor_contact_all(self, single_donor):
        # Get List of donor contacts
        db = get_connection()
        cursor = db.cursor()

        try:
            cursor.execute(
                f"""SELECT * FROM EMERGENCY_CONTACT_INFO
                WHERE Donor_id = '{single_donor['Donor_id']}'""")
            t = cursor.fetchall()
            i = 0
            mydonor = {}
            mydonorc = {}
            for row in t:
                mydonorc.update(
                    {f'Phone_no{i}': row[0], f'Donor_id{i}': row[1], f'Name{i}': row[2]})
                i = i+1
            mydonor["Emergency_Contacts"] = mydonorc
        except mysql.Error as err:
            print("Failed to get donor contact data: {}".format(err))
            return {"status": 500, "message": str(err)}

        db.close()
        return {"status": 200, "message": mydonor}
