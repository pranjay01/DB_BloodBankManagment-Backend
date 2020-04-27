-- SJSU CMPE 138Spring2020 TEAM7

DROP database if EXISTS Blood_Donation_Project;

CREATE database Blood_Donation_Project;

use Blood_Donation_Project;

CREATE TABLE OPERATOR
(
Operator_id INT NOT NULL,
Name VARCHAR(25)  NOT NULL,
Email VARCHAR(25) NOT NULL UNIQUE,
Password VARCHAR(20) NOT NULL,
Bbank_id INT NOT NULL
);

CREATE TABLE BLOOD_BANK (
Bbank_id INT NOT NULL,
Name VARCHAR(45)  NOT NULL,
Type VARCHAR(15),
phone_no BIGINT NOT NULL CHECK (phone_no BETWEEN 1000000000 and 9999999999));

create table BLOOD_DONATION_EVENT (
Drive_id INT NOT NULL,
Name VARCHAR(45)  NOT NULL,
-- YYYY-MM-DD
Date_of_event DATETIME NOT NULL,
Venue VARCHAR(50) NOT NULL,
Operator_id INT );

CREATE TABLE NOTIFIED_BY(
Operator_id INT NOT NULL,
Br_id INT NOT NULL);

Create table BRANCH_PHONE
(
Br_id INT NOT NULL,
Phone_no BIGINT NOT NULL CHECK (phone_no BETWEEN 1000000000 and 9999999999));

CREATE TABLE BLOOD_STOCK (
  Br_id INT NOT NULL,
  Blood_group VARCHAR(3) NOT NULL,
  Btype_Limits INT DEFAULT 100);

CREATE TABLE BRANCH(
Br_id	INT NOT NULL,
Br_Type	ENUM('Main Branch','Sub Branch') NOT NULL,
Bbank_id INT NOT NULL,
Street VARCHAR(20) NOT NULL UNIQUE,
City VARCHAR(20) NOT NULL,
Zip INT NOT NULL CHECK (Zip BETWEEN 10000 and 99999) );

CREATE TABLE BLOOD (
  Blood_id INT NOT NULL ,
  Blood_Group ENUM('O+','A+','B+','AB+','O-','A-','B-','AB-') NOT NULL,
  Br_id INT,
  Donor_id INT ,
  -- Date format : 'YYYY-MM-DD'
  Donation_Date DATE NOT NULL,
  Date_of_Expiry DATE GENERATED ALWAYS AS (DATE_ADD(Donation_Date, INTERVAL 2 MONTH)) NOT NULL,
  Special_Attributes VARCHAR(45));

CREATE TABLE DONOR
(
Donor_id INT NOT NULL,
Name VARCHAR(25) NOT NULL,
Blood_group ENUM('O+','A+','B+','AB+','O-','A-','B-','AB-') NOT NULL,
Street VARCHAR(20),
City VARCHAR(20),
Zip INT CHECK (Zip BETWEEN 10000 and 99999),
Paid_Unpaid BOOL DEFAULT false,
Notification_Subscription BOOL DEFAULT false,
Notification_Type ENUM('E-MAIL','MESSAGE') ,
Operator_id INT);

Create table DONOR_EMAIL
(
Donor_id INT NOT NULL,
Email_id VARCHAR(25) NOT NULL UNIQUE);

Create table AFFILIATED
(
Donor_id INT NOT NULL,
Br_id INT NOT NULL);

CREATE TABLE DONOR_PHONE (
  Phone_no BIGINT NOT NULL CHECK (phone_no BETWEEN 1000000000 and 9999999999),
  Donor_id INT NOT NULL);

CREATE TABLE EMERGENCY_CONTACT_INFO (
  Phone_no BIGINT NOT NULL,
  Donor_id INT NOT NULL,
  Name VARCHAR(25) NULL);

CREATE TABLE EMERGENCY_CONTACT_EMAIL (
  Phone_no BIGINT NOT NULL,
  Donor_id INT NOT NULL,
  Email_id VARCHAR(25) NOT NULL UNIQUE);

CREATE TABLE DBA_LOGIN_CREDENTIALS (
  DBA_id INT NOT NULL ,
  Email_id VARCHAR(25) NOT NULL UNIQUE,
  Password VARCHAR(20) NOT NULL);
  

  
  
-- Constraints 

-- Private keys
ALTER TABLE OPERATOR
ADD CONSTRAINT PK_Operator PRIMARY KEY (Operator_id);

ALTER TABLE BLOOD_BANK
ADD CONSTRAINT PK_Blood_Bank PRIMARY KEY (Bbank_id);

ALTER TABLE BLOOD_DONATION_EVENT
ADD CONSTRAINT PK_Event PRIMARY KEY (Drive_id);

ALTER TABLE NOTIFIED_BY
ADD CONSTRAINT PK_Notify_By PRIMARY KEY (Operator_id,Br_id);

ALTER TABLE BRANCH_PHONE
ADD CONSTRAINT PK_Branch_Phone PRIMARY KEY (Br_id,Phone_no);

ALTER TABLE BLOOD_STOCK
ADD CONSTRAINT PK_stock PRIMARY KEY (Br_id, Blood_group);

ALTER TABLE BRANCH
ADD CONSTRAINT PK_Branch PRIMARY KEY (Br_id);

ALTER TABLE BLOOD
ADD CONSTRAINT Pk_Blood PRIMARY KEY (Blood_id);

ALTER TABLE DONOR
ADD CONSTRAINT Pk_Donor PRIMARY KEY (Donor_id);

ALTER TABLE DONOR_EMAIL
ADD CONSTRAINT PK_Donor_Email PRIMARY KEY (Donor_id, Email_id);

ALTER TABLE AFFILIATED
ADD CONSTRAINT PK_Affilated PRIMARY KEY (Donor_id, Br_id);

-- Doubt, primary key will be composite, or only Phone_no
ALTER TABLE DONOR_PHONE
ADD CONSTRAINT PK_Phone PRIMARY KEY (Phone_no,Donor_id);

ALTER TABLE EMERGENCY_CONTACT_INFO
ADD CONSTRAINT PK_Contact PRIMARY KEY (Phone_no,Donor_id);

ALTER TABLE EMERGENCY_CONTACT_EMAIL
ADD CONSTRAINT PK_Contact_Email PRIMARY KEY (Email_id, Donor_id, Phone_no);

ALTER TABLE DBA_LOGIN_CREDENTIALS
ADD CONSTRAINT PK_Dba PRIMARY KEY (DBA_id) ;


-- AUTOINCREMENT constraints
ALTER TABLE BLOOD MODIFY Blood_id INTEGER NOT NULL AUTO_INCREMENT;
ALTER TABLE BLOOD_BANK MODIFY Bbank_id INTEGER NOT NULL AUTO_INCREMENT;
ALTER TABLE BLOOD_DONATION_EVENT MODIFY Drive_id INTEGER NOT NULL AUTO_INCREMENT;
ALTER TABLE BRANCH MODIFY Br_id INTEGER NOT NULL AUTO_INCREMENT;
ALTER TABLE DONOR MODIFY Donor_id INTEGER NOT NULL AUTO_INCREMENT;
ALTER TABLE DBA_LOGIN_CREDENTIALS MODIFY DBA_id INTEGER NOT NULL AUTO_INCREMENT;
ALTER TABLE OPERATOR MODIFY Operator_id INTEGER NOT NULL AUTO_INCREMENT;




-- Foreign Keys
ALTER TABLE OPERATOR
ADD FOREIGN KEY (Bbank_id)
  REFERENCES BLOOD_BANK (Bbank_id)
  ON DELETE CASCADE
  ON UPDATE CASCADE;

ALTER TABLE BLOOD_DONATION_EVENT
ADD FOREIGN KEY (Operator_id)
  REFERENCES OPERATOR (operator_id)
  ON DELETE SET NULL
  ON UPDATE CASCADE;

ALTER TABLE NOTIFIED_BY
ADD FOREIGN KEY (Operator_id)
  REFERENCES OPERATOR (operator_id)
  ON DELETE CASCADE
  ON UPDATE CASCADE;

ALTER TABLE NOTIFIED_BY
ADD FOREIGN KEY (Br_id)
  REFERENCES BRANCH (Br_id)
  ON DELETE CASCADE
  ON UPDATE CASCADE;

ALTER TABLE BRANCH_PHONE
ADD FOREIGN KEY (Br_id)
  REFERENCES BRANCH (Br_id)
  ON DELETE CASCADE
  ON UPDATE CASCADE;

ALTER TABLE BLOOD_STOCK
ADD FOREIGN KEY (Br_id)
  REFERENCES BRANCH (Br_id)
  ON DELETE CASCADE
  ON UPDATE CASCADE;

ALTER TABLE BRANCH
ADD FOREIGN KEY (Bbank_id)
  REFERENCES BLOOD_BANK (Bbank_id)
  ON DELETE CASCADE
  ON UPDATE CASCADE;

ALTER TABLE BLOOD
ADD FOREIGN KEY (Br_id)
  REFERENCES BRANCH (Br_id)
  ON DELETE SET NULL
  ON UPDATE CASCADE;
  
  ALTER TABLE BLOOD
ADD FOREIGN KEY (Donor_id)
  REFERENCES DONOR (Donor_id)
  ON DELETE SET NULL
  ON UPDATE CASCADE;

  ALTER TABLE DONOR
ADD FOREIGN KEY (Operator_id)
  REFERENCES OPERATOR (Operator_id)
  ON DELETE SET NULL
  ON UPDATE CASCADE;

  ALTER TABLE DONOR_EMAIL
ADD FOREIGN KEY (Donor_id)
  REFERENCES DONOR (Donor_id)
  ON DELETE CASCADE
  ON UPDATE CASCADE;

  ALTER TABLE AFFILIATED
ADD FOREIGN KEY (Donor_id)
  REFERENCES DONOR (Donor_id)
  ON DELETE CASCADE
  ON UPDATE CASCADE;

  ALTER TABLE AFFILIATED
ADD FOREIGN KEY (Br_id)
  REFERENCES BRANCH (Br_id)
  ON DELETE CASCADE
  ON UPDATE CASCADE;

ALTER TABLE DONOR_PHONE
ADD FOREIGN KEY (Donor_id)
  REFERENCES DONOR (Donor_id)
  ON DELETE CASCADE
  ON UPDATE CASCADE;

ALTER TABLE EMERGENCY_CONTACT_INFO
ADD FOREIGN KEY (Donor_id)
  REFERENCES DONOR (Donor_id)
  ON DELETE CASCADE
  ON UPDATE CASCADE;

ALTER TABLE EMERGENCY_CONTACT_EMAIL
ADD FOREIGN KEY (Donor_id,Phone_no)
  REFERENCES EMERGENCY_CONTACT_INFO (Donor_id,Phone_no)
  ON DELETE CASCADE
  ON UPDATE CASCADE;
  
  
  
-- DML Queries

-- STORED PROCEDURE to get branch and BloodGroup wise stock details, 

DELIMITER $$
USE Blood_Donation_Project $$
CREATE PROCEDURE branch_wise_stock (IN bnk_id INT)
BEGIN
SELECT BLOOD.Br_id,Br_Type, count(Blood_id) as Blood_Unit_Count
from BLOOD join BRANCH on (BRANCH.Br_id=BLOOD.Br_id AND Bbank_id=bnk_id AND Date_of_Expiry > CURDATE())
group by BLOOD.Br_id;
END$$

DELIMITER ;



DELIMITER $$
USE Blood_Donation_Project $$
CREATE PROCEDURE branch_stock (IN brnc_id INT) 
BEGIN
SELECT Blood_Group, count(Blood_id) as Blood_Unit_Count
from BLOOD 
where Date_of_Expiry > CURDATE()
group by Blood_Group;
END$$

DELIMITER ;



DELIMITER $$
USE Blood_Donation_Project $$
CREATE PROCEDURE bloodbank_wise_stock (IN bnk_id INT) 
BEGIN
SELECT Bbank_id,Name as Blood_Bank_Name, count(Blood_id) as Blood_Unit_Count
from BLOOD_BANK left join (
SELECT Blood_id , BRANCH.Bbank_id as Bank_id
from BRANCH left join BLOOD on 
(BRANCH.Br_id=BLOOD.Br_id AND Date_of_Expiry > CURDATE())
) as tmp on (tmp.Bank_id=BLOOD_BANK.Bbank_id)
group by Bbank_id,Name;
END$$

DELIMITER ;



DELIMITER $$
USE Blood_Donation_Project $$
CREATE PROCEDURE all_blood_bank_stock () 
                        BEGIN
                        SELECT Bbank_id,Name as Blood_Bank_Name, count(Blood_id) as Blood_Unit_Count
                        from BLOOD_BANK left join (
                        SELECT Blood_id , BRANCH.Bbank_id as Bank_id
                        from BRANCH left join BLOOD on 
                        (BRANCH.Br_id=BLOOD.Br_id AND Date_of_Expiry > CURDATE())
                        ) as tmp on (tmp.Bank_id=BLOOD_BANK.Bbank_id)
                        group by Bbank_id,Name;
                        END$$

DELIMITER ;

-- procedure to get information if total blood units fall below the defined limit
DELIMITER $$
USE Blood_Donation_Project $$
CREATE PROCEDURE limit_check (IN bnk_id INT) 
BEGIN
select stk.Br_id,br.Br_Type,stk.Blood_Group,br.City,br.Street,Btype_Limits, 
count(Blood_id) as Blood_Unit_Count from BLOOD_STOCK as stk left join BLOOD as bld on 
(bld.Br_id=stk.Br_id and bld.Blood_Group=stk.Blood_Group) 
join BRANCH as br on (br.Br_id=stk.Br_id)
group by stk.Blood_Group,stk.Br_id,Btype_Limits,br.City,br.Street,br.Br_Type
having stk.Br_id in (Select Br_id from BRANCH where Bbank_id=bnk_id) 
AND Btype_Limits > Blood_Unit_Count;
END$$

DELIMITER ;

-- Query for blood-Stock entity Quantity derived from blood entity 

