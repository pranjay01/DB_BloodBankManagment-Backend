import mysql.connector as mysql
from connection import get_connection
from user import Operator


import mysql.connector as mysql
from create_donor_table import get_connection


class InsertInTable:

    @classmethod
    def donor(self, single_donor):
        db = get_connection('root', 'Parihar2019')
        cursor = db.cursor()
        if Operator.check_branch_id(single_donor["Operator_id"], single_donor["Br_id"]):
            insert_query = """INSERT INTO DONOR
            (Donor_id,Name,Blood_group,Street,City,Zip,Paid_Unpaid,Notification_Subscription,Notification_Type,Operator_id)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            t = (None, single_donor['Name'], single_donor['Blood_group'],
                 single_donor['Street'], single_donor['City'], single_donor['Zip'], single_donor['Paid_Unpaid'],
                 single_donor['Notification_Subscription'], single_donor['Notification_Type'],
                 single_donor['Operator_id'])

            try:
                cursor.execute(insert_query, t)
                db.commit()
                var_Donor = cursor.execute("SELECT MAX(Donor_id) FROM DONOR;")
            except mysql.Error as err:
                print("Failed to add donor entry: {}".format(err))
                return {"status": 500, "entry": str(err)}

            t = tuple(single_donor['Emails'].values())
            insert_query = "INSERT INTO DONOR_EMAIL (Donor_id,Email_id)  VALUES (%s,%s)"
            for x in t:
                try:
                    cursor.execute(insert_query, (var_Donor, x))
                    db.commit()
                except mysql.Error as err:
                    print("Failed to add donor email entry: {}".format(err))
                    return {"status": 500, "entry": str(err)}

            t = tuple(single_donor['Phones'].values())
            insert_query = "INSERT INTO DONOR_PHONE (Donor_id,Phone_no)  VALUES (%s,%s)"
            for x in t:
                try:
                    cursor.execute(insert_query, (var_Donor, x))
                    db.commit()
                except mysql.Error as err:
                    print("Failed to add donor phone entry: {}".format(err))
                    return {"status": 500, "entry": str(err)}

            t = (var_Donor, single_donor['Br_id'])
            insert_query = "INSERT INTO AFFILIATED (Donor_id,Br_id)  VALUES (%s,%s)"
            try:
                cursor.execute(insert_query, t)
                db.commit()
            except mysql.Error as err:
                print("Failed to add affiliated entry: {}".format(err))
                return {"status": 500, "entry": str(err)}

            db.close()
            return {"status": 200, "entry": single_donor}
        else:
            return {"status": 401, "message": "Unauthorised Access"}

    @classmethod
    def donor_contact(self, single_donor):
        db = get_connection('root', 'Parihar2019')
        cursor = db.cursor()
        if Operator.check_bankid(single_donor["Operator_id"], parameters["Bbank_id"]):
            insert_query = "INSERT INTO EMERGENCY_CONTACT_INFO (Phone_no,Donor_id,Name)  VALUES (%s,%s,%s)"
            t = (single_donor['Phone_no'],
                 single_donor['Donor_id'], single_donor['Name'])
            try:
                cursor.execute(insert_query, t)
                db.commit()
            except mysql.Error as err:
                print("Failed to add donor contact entry: {}".format(err))
                return {"status": 500, "entry": str(err)}

            single_contact = single_donor['EMERGENCY_CONTACT']

            t = tuple(single_contact['Phones'].values())
            insert_query = "INSERT INTO DONOR_PHONE (Donor_id,Phone_no)  VALUES (%s,%s)"
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
        db = get_connection('root', 'Parihar2019')
        cursor = db.cursor()
        if Operator.check_bankid(single_donor["Operator_id"], parameters["Bbank_id"]):
            if 'Phones' in dict.keys():
                insert_query = """UPDATE DONOR SET Name = %s,
                Blood_group = %s,Street =%s,City= %s,Zip = %s,Paid_Unpaid =%s,
                Notification_Subscription = %s,Notification_Type = %s
                WHERE Donor_id =%s ;"""
                t = (single_donor['Name'], single_donor['Blood_group'],
                     single_donor['Street'], single_donor['City'], single_donor['Zip'], single_donor['Paid_Unpaid'],
                     single_donor['Notification_Subscription'], single_donor['Notification_Type'], single_donor['Donor_id'])

            else:
                print("boo")
            db.close()
            return {"status": 200, "entry": single_donor}
        else:
            return {"status": 401, "message": "Unauthorised Access"}

    @classmethod
    def donor_contact(self, single_donor):
        db = get_connection('root', 'Parihar2019')
        cursor = db.cursor()

        if Operator.check_bankid(single_donor["Operator_id"], parameters["Bbank_id"]):
            if 'Phones' in dict.keys():
                insert_query = """UPDATE DONOR SET Name = single_donor['Name'],
                Blood_group = single_donor['Blood_group'],
                Street =single_donor['Street'],City= single_donor['City'],
                Zip = single_donor['Zip'],Paid_Unpaid = single_donor['Paid_Unpaid'],
                Notification_Subscription = single_donor['Notification_Subscription'],
                Notification_Type = single_donor['Notification_Type'],
                Operator_id = single_donor['Operator_id']
                WHERE ;"""
            else:
                print("boo")
            db.close()
            return {"status": 200, "entry": single_donor}
        else:
            return {"status": 401, "message": "Unauthorised Access"}


class DeleteInTable:

    @classmethod
    def donor(self, single_donor):
        db = get_connection('root', 'Parihar2019')
        cursor = db.cursor()
        if Operator.check_bankid(single_donor["Operator_id"], parameters["Bbank_id"]):
            insert_query = f"DELETE FROM DONOR_PHONE WHERE Donor_id = '{single_donor['Donor_id']}'"
            try:
                cursor.execute(insert_query)
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
        db = get_connection('root', 'Parihar2019')
        cursor = db.cursor()
        if Operator.check_bankid(single_donor["Operator_id"], parameters["Bbank_id"]):
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
        db = get_connection('root', 'Parihar2019')
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
        db = get_connection('root', 'Parihar2019')
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
        db = get_connection('root', 'Parihar2019')
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
