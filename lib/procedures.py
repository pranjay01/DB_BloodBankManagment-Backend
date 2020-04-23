#SJSU CMPE 138Spring2020 TEAM7

import mysql.connector as mysql
from mysql.connector import errorcode
from create_table import get_connection




branch_wise_stock="""CREATE PROCEDURE branch_wise_stock (IN bnk_id INT) 
                     BEGIN
                     SELECT bh.Br_id,bh.Br_Type,bh.Street,bh.City,bh.Zip, count(Blood_id) as Blood_Unit_Count
                     from BLOOD right join BRANCH as bh on (bh.Br_id=BLOOD.Br_id AND Date_of_Expiry > CURDATE())
                     where Bbank_id=bnk_id
                     group by bh.Br_id,bh.Br_Type,bh.Street,bh.City,bh.Zip;
                     END"""

branch_stock="""CREATE PROCEDURE branch_stock (IN brnc_id INT) 
                BEGIN
                SELECT Blood_Group, count(Blood_id) as Blood_Unit_Count
                from BLOOD 
                where Date_of_Expiry > CURDATE()
                group by Blood_Group,Br_id having Br_id=brnc_id;
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

limit_check = """CREATE PROCEDURE limit_check (IN bnk_id INT) 
                        BEGIN
                        select stk.Br_id,br.Br_Type,stk.Blood_Group,br.City,br.Street,Btype_Limits, count(Blood_id) as Blood_Unit_Count from BLOOD_STOCK as stk left join BLOOD as bld on 
                        (bld.Br_id=stk.Br_id and bld.Blood_Group=stk.Blood_Group) 
                        join BRANCH as br on (br.Br_id=stk.Br_id)
                        group by stk.Blood_Group,stk.Br_id,Btype_Limits,br.City,br.Street,br.Br_Type
                        having stk.Br_id in (Select Br_id from BRANCH where Bbank_id=bnk_id) 
                        AND Btype_Limits > Blood_Unit_Count;
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
    create_procedure(cursor,limit_check)


    db.commit()
    db.close()