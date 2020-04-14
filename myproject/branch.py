from flask import Flask, render_template, url_for, request
import mysql.connector as mysql
from datetime import datetime

class Branch:
  @classmethod
  def insert_branch(self,branchUnit):
        db=get_connection()
        cursor = db.cursor()
        #date=datetime.today().strftime('%Y-%m-%d')
        insert_query="INSERT INTO BRANCH (Br_id,Br_Type,Bbank_id,Street,City,Zip)  VALUES (%s,%s,%s,%s,%s,%s)"
        cursor.execute(insert_query,(branchUnit['branch_id'], \
        branchUnit['branch_type'], branchUnit['branch_bbank'],branchUnit['branch_street'],branchUnit['branch_city'],\
            branchUnit['branch_zip']))

        db.commit()
        db.close()
        return "success"