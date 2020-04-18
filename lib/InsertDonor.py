import mysql.connector as mysql
from connection import get_connection
from user import Operator


class InsertInTable:
    @classmethod
    def donor(self, single_donor):
        db = get_connection()
        cursor = db.cursor()

        if Operator.check_branch_id(single_donor["Operator_id"],single_donor["Br_id"]):
            insert_query = """INSERT INTO DONOR
            (Donor_id,Name,Blood_group,Street,City,Zip,Paid_Unpaid,Notification_Subscription,Notification_Type,Operator_id)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            t = (single_donor['Donor_id'], single_donor['Name'], single_donor['Blood_group'],
                single_donor['Street'], single_donor['City'], single_donor['Zip'], single_donor['Paid_Unpaid'],
                single_donor['Notification_Subscription'], single_donor['Notification_Type'],
                single_donor['Operator_id'])
            try:
                cursor.execute(insert_query, t)
                db.commit()
            except mysql.Error as err:
                print("Failed to add entry: {}".format(err))
                return {"status": 400, "entry": str(err)}

            t = tuple(single_donor['Emails'].values())
            insert_query = "INSERT INTO DONOR_EMAIL (Donor_id,Email_id)  VALUES (%s,%s)"
            for x in t:
                try:
                    cursor.execute(insert_query, (single_donor['Donor_id'], x))
                    db.commit()
                except mysql.Error as err:
                    print("Failed to add entry: {}".format(err))
                    return {"status": 400, "message": str(err)}

            t = tuple(single_donor['Phones'].values())
            insert_query = "INSERT INTO DONOR_PHONE (Donor_id,Phone_no)  VALUES (%s,%s)"
            for x in t:
                try:
                    cursor.execute(insert_query, (single_donor['Donor_id'], x))
                    db.commit()
                except mysql.Error as err:
                    print("Failed to add entry: {}".format(err))
                    return {"status": 400, "message": str(err)}

            db.close()
            return {"status": 200, "donor": single_donor}
        else:
            return {"status": 401, "message": "Unauthorised Access"}

    @classmethod
    def donor_contact(self, single_donor):
        db = get_connection()
        cursor = db.cursor()

        insert_query = "INSERT INTO EMERGENCY_CONTACT_INFO (Phone_no,Donor_id,Name)  VALUES (%s,%s,%s)"
        t = (single_donor['Phone_no'],
             single_donor['Donor_id'], single_donor['Name'])
        try:
            cursor.execute(insert_query, t)
            db.commit()
        except mysql.Error as err:
            print("Failed to add entry: {}".format(err))
            return {"status": 400, "entry": str(err)}

        single_contact = single_donor['EMERGENCY_CONTACT']

        t = tuple(single_contact['Phones'].values())
        insert_query = "INSERT INTO DONOR_PHONE (Donor_id,Phone_no)  VALUES (%s,%s)"
        for x in t:
            try:
                cursor.execute(insert_query, (single_donor['Donor_id'], x))
                db.commit()
            except mysql.Error as err:
                print("Failed to add entry: {}".format(err))
                return {"status": 400, "entry": str(err)}

        db.close()
        return {"status": 200, "entry": single_donor}


class UpdateInTable:

    @classmethod
    def donor(self, single_donor):
        db = get_connection()
        cursor = db.cursor()
        db.close()
        return {"status": 200, "entry": single_donor}

    @classmethod
    def donor_contact(self, single_donor):
        db = get_connection()
        cursor = db.cursor()

        db.close()
        return {"status": 200, "entry": single_donor}


class DeleteInTable:

    @classmethod
    def donor(self, single_donor):
        db = get_connection()
        cursor = db.cursor()
        insert_query = f"DELETE FROM DONOR_PHONE WHERE Donor_id = '{single_donor['Donor_id']}'"
        try:
            cursor.execute(insert_query)
            db.commit()
        except mysql.Error as err:
            print("Failed to delete entry: {}".format(err))
            return {"status": 400, "entry": str(err)}
        db.close()
        return {"status": 200, "entry": single_donor}

    @classmethod
    def donor_contact(self, single_donor):
        db = get_connection()
        cursor = db.cursor()

        try:
            cursor.execute(
                f"""SELECT * FROM EMERGENCY_CONTACT_INFO 
                WHERE Donor_id = '{single_donor['Donor_id']}'""")
            t = cursor.fetchall()
            if (len(t) > 1):
                insert_query = f"""SELECT * FROM EMERGENCY_CONTACT_INFO 
                WHERE Donor_id = '{single_donor['Donor_id']}' 
                AND Phone_no = '{single_donor['Phone_no']}'"""
                try:
                    cursor.execute(insert_query)
                    db.commit()
                except mysql.Error as err:
                    print("Failed to delete entry: {}".format(err))
                    return {"status": 400, "entry": str(err)}
            else:
                s = "Each Donor requires at least one Donor.Delete Fail"
                print(s)
                return {"status": 400, "entry": s}
        except mysql.Error as err:
            print("Failed to get donor contact data: {}".format(err))
            return {"status": 400, "entry": str(err)}

        db.close()
        return {"status": 200, "entry": single_donor}


class SelectInTable:

    @classmethod
    def donor(self, single_donor):
        db = get_connection()
        cursor = db.cursor()

        try:
            cursor.execute(
                f"SELECT * FROM DONOR WHERE Donor_id = '{single_donor['Donor_id']}'")
            t = cursor.fetchone()
            mydonor = {'Donor_id': t[0], 'Name': t[1], 'Blood_group': t[2],
                       'Street': t[3], 'City': t[4], 'Zip': t[5], 'Paid_Unpaid': t[6],
                       'Notification_Subscription': t[7], 'Notification_Type': t[8],
                       'Operator_id': t[9]}
        except mysql.Error as err:
            print("Failed to get donor data: {}".format(err))
            return {"status": 400, "entry": str(err)}

        try:
            cursor.execute(
                f"SELECT * FROM DONOR_EMAIL WHERE Donor_id = '{single_donor['Donor_id']}'")
            t = cursor.fetchall()
            i = 0
            mydemail = {}
            for row in t:
                mydemail.update({f'Email{i}': row[1]})
                i = i+1
            mydonor["Emails"] = mydemail
        except mysql.Error as err:
            print("Failed to get donor emails: {}".format(err))
            return {"status": 400, "entry": str(err)}

        try:
            cursor.execute(
                f"SELECT * FROM DONOR_PHONE WHERE Donor_id = '{single_donor['Donor_id']}'")
            t = cursor.fetchall()
            i = 0
            mydphone = {}
            for row in t:
                mydphone.update({f'Phone{i}': row[1]})
                i = i+1
            mydonor["Phones"] = mydphone
        except mysql.Error as err:
            print("Failed to get donor Phones: {}".format(err))
            return {"status": 400, "entry": str(err)}

        db.close()
        return {"status": 200, "entry": mydonor}

    @classmethod
    def donor_contact(self, single_donor):
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
            return {"status": 400, "entry": str(err)}

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
            return {"status": 400, "entry": str(err)}

        db.close()
        return {"status": 200, "entry": mydonor}
