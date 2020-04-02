DROP database if EXISTS Blood_Donation_Project;

CREATE database Blood_Donation_Project;

use Blood_Donation_Project;

CREATE TABLE OPERATOR
(
Operator_id INT NOT NULL,
Name VARCHAR(25)  NOT NULL,
Email VARCHAR(25) NOT NULL,
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
Street VARCHAR(20) NOT NULL,
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
Notification_Type ENUM('MAIL','MESSAGE') ,
Operator_id INT);

Create table DONOR_EMAIL
(
Donor_id INT NOT NULL,
Email_id VARCHAR(25) NOT NULL);

Create table AFFILIATED
(
Donor_id INT NOT NULL,
Br_id INT NOT NULL);

CREATE TABLE DONOR_PHONE (
  Phone_no BIGINT NOT NULL CHECK (phone_no BETWEEN 1000000000 and 9999999999),
  Donor_id INT NOT NULL);

CREATE TABLE EMERGENCY_CONTACT_INFO (
  Phone_no BIGINT NOT NULL CHECK (phone_no BETWEEN 1000000000 and 9999999999),
  Donor_id INT NOT NULL,
  Name VARCHAR(25) NULL);

CREATE TABLE EMERGENCY_CONTACT_EMAIL (
  Phone_no BIGINT NOT NULL CHECK (phone_no BETWEEN 1000000000 and 9999999999),
  Donor_id INT NOT NULL,
  Email_id VARCHAR(25) NOT NULL);

CREATE TABLE DBA_LOGIN_CREDENTIALS (
  DBA_id INT NOT NULL ,
  Email_id VARCHAR(25) NOT NULL UNIQUE,
  Password VARCHAR(20) NOT NULL);
  

  
  
-- Constraints 

-- Private keys
ALTER TABLE OPERATOR
ADD CONSTRAINT PK_Operator PRIMARY KEY AUTO_INCREMENT (Operator_id);

ALTER TABLE BLOOD_BANK
ADD CONSTRAINT PK_Blood_Bank PRIMARY KEY AUTO_INCREMENT (Bbank_id);

ALTER TABLE BLOOD_DONATION_EVENT
ADD CONSTRAINT PK_Event PRIMARY KEY AUTO_INCREMENT (Drive_id);

ALTER TABLE NOTIFIED_BY
ADD CONSTRAINT PK_Notify_By PRIMARY KEY (Operator_id,Br_id);

ALTER TABLE BRANCH_PHONE
ADD CONSTRAINT PK_Branch_Phone PRIMARY KEY (Br_id,Phone_no);

ALTER TABLE BLOOD_STOCK
ADD CONSTRAINT PK_stock PRIMARY KEY (Br_id, Blood_group);

ALTER TABLE BRANCH
ADD CONSTRAINT PK_Branch PRIMARY KEY AUTO_INCREMENT (Br_id);

ALTER TABLE BLOOD
ADD CONSTRAINT Pk_Blood PRIMARY KEY AUTO_INCREMENT (Blood_id);

ALTER TABLE DONOR
ADD CONSTRAINT Pk_Donor PRIMARY KEY AUTO_INCREMENT (Donor_id);

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
ADD CONSTRAINT PK_Dba PRIMARY KEY AUTO_INCREMENT (DBA_id) ;




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

USE Blood_Donation_Project;
DROP procedure IF EXISTS list_branch_stocks;

DELIMITER $$
USE Blood_Donation_Project $$
CREATE PROCEDURE list_branch_stocks (
IN Branch_id INT,
IN Blood_Grp VARCHAR(5)
) 
BEGIN
select Br_id, Blood_Group, count(Blood_id) as Count
from BLOOD
group by (Br_id, Blood_Group)
having Br_id=Branch_id and Blood_Group=Blood_Grp;
END$$

DELIMITER ;


-- Query for blood-Stock entity Quantity derived from blood entity 

