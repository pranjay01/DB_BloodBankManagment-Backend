
create table OPERATOR
(
Operator_id		char(9)		not NULL,
Name		varchar(25),
Email		varchar(25),
Password		varchar(25),
Br_id		char(9)		not NULL,
primary key (Operator_id),
foreign key (Br_id) references BRANCH(Br_id)
);

create table BLOOD_BANK
(
Bbank_id	char(9)		not NULL,
Name 		varchar(25),
Type		varchar(15)	not NULL,
phone_no	varchar(10),
primary key (Bbank_id));

create table BLOOD_DONATION_EVENT
(
Drive_id		char(9) 	not NULL,
Name 		varchar(50) not NULL,
Date_of_event	date,
Venue		int(50),
Operator_id	char(9) 	not NULL,
primary key (Drive_id),
foreign key (Operator_id) references OPERATOR(operator_id)
);


Create table BRANCH_PHONE
(
Br_id		char(9)	not NULL,
Phone		varchar(10),
primary key (Br_id,phone),
Foreign key (Br_id) references BRANCH(Br_id)	
);


Create table AFFILIATED
(
Donor_id		char(9)	not NULL,
Br_id		char(9) 	not NULL,
primary key (Donor_id,Br_id),
foreign key (Donor_id) references donor(Donor_id),
Foreign key (Br_id) references branch(Br_id)
);

Create table DONOR
(
Donor_id	char(9) 	not NULL,
Name		varchar(100),
Blood_group	char(2)		not NULL,
Street		varchar(30),
City		varchar(25),
Paid_Unpaid	BOOL,
Notification_Subscription	BOOL,
Notification_Type
Operation_id	char(9)		not NULL,
Foreign key (Operator_id) references OPERATOR(Operator_id)
);

Create table BLOOD_STOCK
(
Br_id	char(9)		not NULL,
Blood_Group	char(2)		not NULL,
Btype_Limits	INT,
Quantity	INT AS (/*   Query for BLOOD_STOCK Quantity */
SELECT COUNT(Blood_id) as Unit
FROM BLOOD as BL INNER JOIN BLOOD_STOCK as B_Stock ON BL.Br_id = B_Stock.Br_id
Where BL.Blood_Group = B_Stock.Blood_Group
GROUP BY Unit),
Primary (Br_id,Blood_Group)
);

Create table BLOOD
(
Blood_id	char(9)		not NULL,
Special_Attributes	varchar(25),
Blood_Group	char(2)		not NULL,
Br_id		char(9)		not NULL,
Donor_id	char(9)		not NULL,
Donation_Date	DATETIME	not NULL,
Date_of_Expiry	DATETIME AS (SELECT DATEADD(month, 2, Donation_Date)),
Primary key (Blood_id),
Foreign key (Br_id) references BRANCH(Br_id),
Foreign key (Donor_id) references DONOR(Donor_id)
);



Create table DONOR_EMAIL
(
Donor_id	char(9)		not NULL,
Email_id	char(9)		not NULL,
Primary key (Email_id),
Foreign key (Donor_id) references	DONOR(Donor_id)
);



/*   Query for BLOOD_STOCK Quantity 
SELECT COUNT(Blood_id) as Unit
FROM BLOOD as BL INNER JOIN BLOOD_STOCK as B_Stock ON BL.Br_id = B_Stock.Br_id
Where BL.Blood_Group = B_Stock.Blood_Group
GROUP BY Unit;

*/

