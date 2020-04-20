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
        if Operator.check_branch_id(single_donor["Operator_id"], single_donor["Br_id"]):

            insert_query = """INSERT INTO DONOR
            (Donor_id,Name,Blood_group,Street,City,Zip,Paid_Unpaid,Notification_Subscription,Notification_Type,Operator_id)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            t = (None, single_donor['Name'], single_donor['Blood_group'],
                 single_donor['Street'], single_donor['City'], single_donor['Zip'], single_donor['Paid_Unpaid'],
                 single_donor['Notification_Subscription'], single_donor['Notification_Type'], single_donor['Operator_id'])

            try:
                cursor.execute(insert_query, t)
                db.commit()

                # Last Donor ID is assumed to be the MAX()
                # LAST_INSERT_ID() is not working with multiple connnects
                var_Donor = cursor.execute("SELECT MAX(Donor_id) FROM DONOR;")
            except mysql.Error as err:
                print("Failed to add donor entry: {}".format(err))
                return {"status": 500, "entry": str(err)}

            # Need to update this based on what Salman is expecting
            t = tuple(single_donor['Emails'].values())
            insert_query = "INSERT INTO DONOR_EMAIL (Donor_id,Email_id)  VALUES (%s,%s)"
            for x in t:
                try:
                    cursor.execute(insert_query, (var_Donor, x))
                    db.commit()
                except mysql.Error as err:
                    print("Failed to add donor email entry: {}".format(err))
                    return {"status": 500, "entry": str(err)}

            # Need to update this based on what Salman is expecting
            # Mulitple phones updated assuming all infromation is present in a nested
            t = tuple(single_donor['Phones'].values())
            insert_query = "INSERT INTO DONOR_PHONE (Donor_id,Phone_no)  VALUES (%s,%s)"
            for x in t:
                try:
                    cursor.execute(insert_query, (var_Donor, x))
                    db.commit()
                except mysql.Error as err:
                    print("Failed to add donor phone entry: {}".format(err))
                    return {"status": 500, "entry": str(err)}

            # Affiiate table entry is inserted directly when a new donor is added
            t = (var_Donor, single_donor['Br_id'])
            insert_query = "INSERT INTO AFFILIATED (Donor_id,Br_id)  VALUES (%s,%s)"
            try:
                cursor.execute(insert_query, t)
                db.commit()
            except mysql.Error as err:
                print("Failed to add affiliated entry: {}".format(err))
                return {"status": 500, "entry": str(err)}

            db.close()
            print("Donor added successfully")
            return {"status": 200, "entry": single_donor}
        else:
            print("Unauthorised Access")
            return {"status": 401, "message": "Unauthorised Access"}

    @classmethod
    def donor_contact(self, single_donor):
        db = get_connection()
        cursor = db.cursor()

        # Remove the single contact field if single_donor json directly sends E contact info
        # single_contact = single_donor['EMERGENCY_CONTACT']
        if Operator.check_bankid(single_donor["Operator_id"], single_donor["Bbank_id"]):
            insert_query = "INSERT INTO EMERGENCY_CONTACT_INFO (Phone_no,Donor_id,Name)  VALUES (%s,%s,%s)"
            t = (single_donor['Phone_no'],
                 single_donor['Donor_id'], single_donor['Name'])
            try:
                cursor.execute(insert_query, t)
                db.commit()
            except mysql.Error as err:
                print("Failed to add donor contact entry: {}".format(err))
                return {"status": 500, "entry": str(err)}

            # Need to update this based on what Salman is expecting
            t = tuple(single_donor['Phones'].values())
            insert_query = "INSERT INTO EMERGENCY_CONTACT_EMAIL (Donor_id,Phone_no)  VALUES (%s,%s)"
            for x in t:
                try:
                    cursor.execute(insert_query, (single_donor['Donor_id'], x))
                    db.commit()
                except mysql.Error as err:
                    print("Failed to add contact phones entry: {}".format(err))
                    return {"status": 500, "entry": str(err)}

            db.close()
            return {"status": 200, "entry": single_donor}
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
                return {"status": 500, "entry": str(err)}

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
                return {"status": 500, "entry": str(err)}

            # Need to update this based on what Salman is expecting
            t = tuple(single_donor['Phomes'].values())
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
                return {"status": 500, "entry": str(err)}

            db.close()
            return {"status": 200, "entry": single_donor}
        else:
            return {"status": 401, "message": "Unauthorised Access"}

    @classmethod
    def donor_contact(self, single_donor):
        db = get_connection()
        cursor = db.cursor()

        if Operator.check_bankid(single_donor["Operator_id"], single_donor["Bbank_id"]):
            update_query = """UPDATE EMERGENCY_CONTACT_INFO SET Name = %s, WHERE Donor_id =%s ;"""
            t = (single_donor['Name'], single_donor['Donor_id'])
            try:
                cursor.execute(update_query, t)
                db.commit()
            except mysql.Error as err:
                print("Failed to update donor contact entry: {}".format(err))
                return {"status": 500, "entry": str(err)}

            # Need to update this based on what Salman is expecting
            t = tuple(single_donor['Emails'].values())
            try:
                delete_query = f"DELETE FROM EMERGENCY_CONTACT_EMAIL WHERE Donor_id = '{single_donor['Donor_id']}'"
                cursor.execute(delete_query)
                db.commit()
                insert_query = "INSERT INTO EMERGENCY_CONTACT_EMAIL (Phone_no,Donor_id,Email_id)  VALUES (%s,%s,%s)"
                for x in t:
                    cursor.execute(
                        insert_query, (single_donor['Phone_no'], single_donor['Donor_id'], x))
                    db.commit()
            except mysql.Error as err:
                print("Failed to update donor comtact email entry: {}".format(err))
                return {"status": 500, "entry": str(err)}

            db.close()
            return {"status": 200, "entry": single_donor}
        else:
            return {"status": 401, "message": "Unauthorised Access"}


class DeleteInTable:

    @classmethod
    def donor(self, single_donor):
        # Member function only deletes donor from the DONOR table
        # Delete on cascade expected to take care of the rest
        db = get_connection()
        cursor = db.cursor()
        single_donor["Br_id"]=int(single_donor["Br_id"])
        single_donor["Operator_id"] = int(single_donor["Operator_id"])
        if Operator.check_branch_id(single_donor["Operator_id"], single_donor["Br_id"]):
            delete_query = f"DELETE FROM DONOR_PHONE WHERE Donor_id = '{single_donor['Donor_id']}'"
            try:
                cursor.execute(delete_query)
                db.commit()
            except mysql.Error as err:
                print("Failed to delete entry: {}".format(err))
                return {"status": 500, "entry": str(err)}
            db.close()
            return {"status": 200, "entry": single_donor}
        else:
            return {"status": 401, "message": "Unauthorised Access"}

    @classmethod
    def donor_contact(self, single_donor):
        # Member function only to delete ONE donor contact from the DONOR_CONTACT table
        db = get_connection()
        cursor = db.cursor()
        if Operator.check_bankid(single_donor["Operator_id"], single_donor["Bbank_id"]):
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
                        return {"status": 500, "entry": str(err)}
                else:
                    s = "Each Donor requires at least one Donor.Delete Fail"
                    print(s)
                    return {"status": 500, "entry": s}
            except mysql.Error as err:
                print("Failed to get donor contact data: {}".format(err))
                return {"status": 500, "entry": str(err)}

            db.close()
            return {"status": 200, "entry": single_donor}
        else:
            return {"status": 401, "message": "Unauthorised Access"}


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
            mydonor = {'Donor_id': t[0], 'Name': t[1], 'Blood_group': t[2],
                       'Street': t[3], 'City': t[4], 'Zip': t[5], 'Paid_Unpaid': t[6],
                       'Notification_Subscription': t[7], 'Notification_Type': t[8],
                       'Operator_id': t[9]}
            var_donor = t[0]
        except mysql.Error as err:
            print("Failed to get donor data: {}".format(err))
            return {"status": 500, "entry": str(err)}

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
            return {"status": 500, "entry": str(err)}

        try:
            cursor.execute(
                f"SELECT * FROM DONOR_PHONE WHERE Donor_id = '{var_donor}'")
            t = cursor.fetchall()
            i = 0
            mydphone = {}
            for row in t:
                mydphone.update({f'Phone{i}': row[1]})
                i = i+1
            mydonor["Phones"] = mydphone
        except mysql.Error as err:
            print("Failed to get donor Phones: {}".format(err))
            return {"status": 500, "entry": str(err)}

        try:
            cursor.execute(
                f"SELECT Br_id FROM AFFILIATED WHERE Donor_id = '{var_donor}'")
            mydonor['Br_id'] = cursor.fetchone()
        except mysql.Error as err:
            print("Failed to get donor data: {}".format(err))
            return {"status": 500, "entry": str(err)}

        db.close()
        return {"status": 200, "entry": mydonor}

    @classmethod
    def donor_contact(self, single_donor):
        # Selects and returns data from all donor contact related tables
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
            return {"status": 500, "entry": str(err)}

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
            return {"status": 500, "entry": str(err)}

        db.close()
        return {"status": 200, "entry": mydonor}

    @classmethod
    def donor_contact_all(self, single_donor):
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
            return {"status": 500, "entry": str(err)}

        db.close()
        return {"status": 200, "entry": mydonor}
