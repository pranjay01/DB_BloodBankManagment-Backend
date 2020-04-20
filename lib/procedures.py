import mysql.connector as mysql
from mysql.connector import errorcode
from create_table import get_connection




branch_wise_stock="""CREATE PROCEDURE branch_wise_stock (IN bnk_id INT) 
                     BEGIN
                     SELECT BLOOD.Br_id,Br_Type, count(Blood_id) as Blood_Unit_Count
                     from BLOOD join BRANCH on (BRANCH.Br_id=BLOOD.Br_id AND Bbank_id=bnk_id AND Date_of_Expiry > CURDATE())
                     group by BLOOD.Br_id;
                     END"""

branch_stock="""CREATE PROCEDURE branch_stock (IN brnc_id INT) 
                BEGIN
                SELECT Blood_Group, count(Blood_id) as Blood_Unit_Count
                from BLOOD 
                where Br_id=brnc_id AND Date_of_Expiry > CURDATE()
                group by Blood_Group;
                END"""

bloodbank_wise_stock="""CREATE PROCEDURE bloodbank_wise_stock (IN bnk_id INT) 
                        BEGIN
                        SELECT Bbank_id,Name as Blood_Bank_Name, count(Blood_id) as Blood_Unit_Count
                        from BLOOD_BANK left join (
                        SELECT Blood_id , BRANCH.Bbank_id as Bank_id
                        from BRANCH left join BLOOD on 
                        (BRANCH.Br_id=BLOOD.Br_id AND Date_of_Expiry > CURDATE())
                        ) as tmp on (tmp.Bank_id=BLOOD_BANK.Bbank_id)
                        group by Bbank_id,Name
                        having Bbank_id=bnk_id;
                        END"""

all_blood_bank_stock="""CREATE PROCEDURE all_blood_bank_stock () 
                        BEGIN
                        SELECT Bbank_id,Name as Blood_Bank_Name, count(Blood_id) as Blood_Unit_Count
                        from BLOOD_BANK left join (
                        SELECT Blood_id , BRANCH.Bbank_id as Bank_id
                        from BRANCH left join BLOOD on 
                        (BRANCH.Br_id=BLOOD.Br_id AND Date_of_Expiry > CURDATE())
                        ) as tmp on (tmp.Bank_id=BLOOD_BANK.Bbank_id)
                        group by Bbank_id,Name;
                        END"""


def create_procedure(cursor,query):
    try:
        cursor.execute(query)
    except mysql.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)    
        



if __name__ == '__main__':  # to not run code on import
    db=get_connection()
    cursor = db.cursor()

    create_procedure(cursor,branch_wise_stock)
    create_procedure(cursor,branch_stock)
    create_procedure(cursor,bloodbank_wise_stock)
    create_procedure(cursor,all_blood_bank_stock)


    db.commit()
    db.close()