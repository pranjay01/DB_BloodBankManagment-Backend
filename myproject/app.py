from flask import Flask, render_template, url_for, request
import mysql.connector as mysql
from branch import Branch
from datetime import datetime


def get_connection():
  mydb = mysql.connect(
    host="localhost",
    user="root",
    passwd="admin123",
    db="Blood_Donation_Project"
  )
  return mydb
db = get_connection()
mycursor = db.cursor()
app = Flask(__name__)




def showTable():
    showTable_query = """ USE Blood_Donation_Project; SHOW TABLES; """
    mycursor.execute(showTable_query,multi=True)
    for x in mycursor:
        print(x)

@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
      pass
    else :
      showTable()
      return render_template('index.html')
# branch route
@app.route('/branch', methods = ['POST', 'GET'])
def insert_branch():
    if request.method == 'POST':
        data = request.get_json()
        branch_id = request.form['branch_ID']
        branch_type = request.form['branch_Type']
        branch_bbank = request.form['branch_Bbank']
        branch_street = request.form['branch_Street']
        branch_city = request.form['branch_City']
        branch_zip = request.form['branch_Zipcode']
    else :
        
      pass
      return render_template('index.html')  
      
if __name__ == "__main__":
    app.run(debug=True)

