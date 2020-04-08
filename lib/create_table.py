import mysql.connector as mysql


def get_connection():
    db = mysql.connect(
        host = "localhost",
        user = "root",
        passwd = "Pranjay@01",
        database = "ProjectDB"
    )
    return db

if __name__ == '__main__':  # to not run code on import
    db=get_connection()
    cursor = db.cursor()

    create_table = """CREATE TABLE IF NOT EXISTS BLOOD (Blood_id INT NOT NULL ,
    Blood_Group ENUM('O+','A+','B+','AB+','O-','A-','B-','AB-') NOT NULL,
    Br_id INT,
    Donor_id INT ,
    Donation_Date DATE NOT NULL,
    Date_of_Expiry DATE GENERATED ALWAYS AS (DATE_ADD(Donation_Date, INTERVAL 2 MONTH)) ,
    Special_Attributes VARCHAR(45))"""
    
    cursor.execute(create_table)


    create_table = """ALTER TABLE BLOOD ADD CONSTRAINT Pk_Blood PRIMARY KEY AUTO_INCREMENT (Blood_id)"""
    cursor.execute(create_table)

    #cursor.execute("INSERT INTO items VALUES ('test', 10.99)")

    db.commit()
    db.close()
