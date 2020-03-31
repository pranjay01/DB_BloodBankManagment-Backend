drop database if exists Blood_Donation_Project;

create database Blood_Donation_Project;

use Blood_Donation_Project;


CREATE TABLE DONOR_PHONE (
  Phone_no VARCHAR(15) NOT NULL,
  DonorId VARCHAR(45) NOT NULL);


CREATE TABLE EMERGENCY_CONTACT_INFO (
  Phone_no VARCHAR(15) NOT NULL,
  Donor_id INT NOT NULL,
  Name VARCHAR(45) NULL);


CREATE TABLE EMERGENCY_CONTACT_EMAIL (
  Phone_no VARCHAR(15) NOT NULL,
  Donor_id INT NOT NULL,
  Email_id VARCHAR(45) NOT NULL,
  EMERGENCY_CONTACT_INFOcol VARCHAR(45) NULL);

CREATE TABLE DBA_LOGIN_CREDENTIALS (
  DBA_id INT NOT NULL ,
  Email_id VARCHAR(45) NOT NULL UNIQUE,
  user_name VARCHAR(20) NOT NULL UNIQUE,
  Password VARCHAR(25) NOT NULL);
  
  CREATE TABLE BLOOD (
  Blood_id INT NOT NULL ,
  Blood_Group VARCHAR(5) NOT NULL,
  Br_id INT NULL NOT NULL,
  Donor_id INT NULL,
  -- Date format : 'YYYY-MM-DD'
  Donation_Date DATE NOT NULL,
  Date_of_Expiry DATE GENERATED ALWAYS AS (DATE_ADD(Donation_Date, INTERVAL 10 DAY)));

CREATE TABLE BLOOD_STOCK (
  Br_id INT NOT NULL,
  Blood_group VARCHAR(5) NOT NULL,
  Btype_Limits INT NOT NULL,
  Quantity INT default 0);

  
  
-- Constraints 

-- Private keys
ALTER TABLE DONOR_PHONE
ADD CONSTRAINT PK_Phone PRIMARY KEY (Phone_no);


ALTER TABLE EMERGENCY_CONTACT_INFO
ADD CONSTRAINT PK_Contact PRIMARY KEY (Phone_no,Donor_id);

ALTER TABLE EMERGENCY_CONTACT_EMAIL
ADD CONSTRAINT PK_Contact_Email PRIMARY KEY (Email_id, Donor_id, Phone_no);

ALTER TABLE DBA_LOGIN_CREDENTIALS
ADD CONSTRAINT PK_Dba PRIMARY KEY AUTO_INCREMENT (DBA_id) ;

ALTER TABLE BLOOD
ADD CONSTRAINT Pk_Blood PRIMARY KEY AUTO_INCREMENT (Blood_id);


ALTER TABLE BLOOD_STOCK
ADD CONSTRAINT PK_stock PRIMARY KEY (Br_id, Blood_group);



-- Foreign Keys
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

ALTER TABLE DONOR_PHONE
ADD FOREIGN KEY (DonorId)
  REFERENCES DONOR (Donor_id)
  ON DELETE CASCADE
  ON UPDATE CASCADE;

ALTER TABLE EMERGENCY_CONTACT_INFO
ADD FOREIGN KEY (DonorId)
  REFERENCES DONOR (Donor_id)
  ON DELETE CASCADE
  ON UPDATE CASCADE;

ALTER TABLE EMERGENCY_CONTACT_EMAIL
ADD FOREIGN KEY (DonorId,Phone_no)
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
