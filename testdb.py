import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="admin123",
  db="Blood_Donation_Project"
)

print(mydb)