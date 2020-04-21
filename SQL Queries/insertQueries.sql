insert into BLOOD_BANK values (1,'bank_abc','clinic',4587631280);
insert into BLOOD_BANK values (2,'bank_abd','clinic',4587631281);
insert into BLOOD_BANK values (3,'bank_abe','clinic',4587631282);
insert into BLOOD_BANK values (4,'bank_abf','clinic',4587631283);
insert into BLOOD_BANK values (5,'bank_abg','clinic',4587631284);
insert into BLOOD_BANK values (6,'bank_acsdc','clinic',4587631285);
insert into BLOOD_BANK values (7,'bank_ascdsv','clinic',4587631286);
insert into BLOOD_BANK values (8,'bank_avfdbs','clinic',4587631287);
insert into BLOOD_BANK values (9,'bank_acsdfvd','clinic',4587631288);
insert into BLOOD_BANK values (10,'bankbgfbf','clinic',4587631289);



insert into BRANCH values (1,'Main Branch',1,'bvcsdchj','ckjdsnkjcn',45896);
insert into BRANCH values (2,'Sub Branch',1,'bvcsdchj','ckjdsnkjcn',45896);
insert into BRANCH values (3,'Main Branch',2,'bvcsdchj','ckjdsnkjcn',45896);
insert into BRANCH values (4,'Sub Branch',2,'bvcsdchj','ckjdsnkjcn',45896);
insert into BRANCH values (5,'Main Branch',3,'bvcsdchj','ckjdsnkjcn',45896);
insert into BRANCH values (6,'Sub Branch',3,'bvcsdchj','ckjdsnkjcn',45896);
insert into BRANCH values (7,'Main Branch',4,'bvcsdchj','ckjdsnkjcn',45896);
insert into BRANCH values (8,'Sub Branch',4,'bvcsdchj','ckjdsnkjcn',45896);
insert into BRANCH values (9,'Main Branch',5,'bvcsdchj','ckjdsnkjcn',45896);
insert into BRANCH values (10,'Sub Branch',5,'bvcsdchj','ckjdsnkjcn',45896);
insert into BRANCH values (11,'Main Branch',6,'bvcsdchj','ckjdsnkjcn',45896);
insert into BRANCH values (12,'Sub Branch',6,'bvcsdchj','ckjdsnkjcn',45896);
insert into BRANCH values (13,'Main Branch',7,'bvcsdchj','ckjdsnkjcn',45896);
insert into BRANCH values (14,'Sub Branch',7,'bvcsdchj','ckjdsnkjcn',45896);


insert into BLOOD (Blood_id,Special_Attributes,Blood_Group,Br_id,Donor_id,Donation_Date)
 values (1,NULL,'O+',1,1,CURDATE());
 insert into BLOOD (Blood_id,Special_Attributes,Blood_Group,Br_id,Donor_id,Donation_Date)
 values (2,NULL,'A+',1,2,CURDATE());
 insert into BLOOD (Blood_id,Special_Attributes,Blood_Group,Br_id,Donor_id,Donation_Date)
 values (3,NULL,'B+',2,3,CURDATE());
 insert into BLOOD (Blood_id,Special_Attributes,Blood_Group,Br_id,Donor_id,Donation_Date)
 values (4,NULL,'AB+',2,4,CURDATE());
 insert into BLOOD (Blood_id,Special_Attributes,Blood_Group,Br_id,Donor_id,Donation_Date)
 values (5,NULL,'O-',3,5,CURDATE());
insert into BLOOD (Blood_id,Special_Attributes,Blood_Group,Br_id,Donor_id,Donation_Date) values (6,NULL ,'A-',4,6,CURDATE());
insert into BLOOD (Blood_id,Special_Attributes,Blood_Group,Br_id,Donor_id,Donation_Date) values (7,NULL ,'B-',4,7,CURDATE());
insert into BLOOD (Blood_id,Special_Attributes,Blood_Group,Br_id,Donor_id,Donation_Date) values (8,NULL ,'AB-',5,8,CURDATE());
insert into BLOOD (Blood_id,Special_Attributes,Blood_Group,Br_id,Donor_id,Donation_Date) values (9,NULL ,'O+',5,1,CURDATE());
insert into BLOOD (Blood_id,Special_Attributes,Blood_Group,Br_id,Donor_id,Donation_Date) values (10,NULL ,'A+',6,2,CURDATE());
insert into BLOOD (Blood_id,Special_Attributes,Blood_Group,Br_id,Donor_id,Donation_Date) values (11,NULL ,'B+',6,3,CURDATE());
insert into BLOOD (Blood_id,Special_Attributes,Blood_Group,Br_id,Donor_id,Donation_Date) values (12,NULL ,'AB+',7,4,CURDATE());
insert into BLOOD (Blood_id,Special_Attributes,Blood_Group,Br_id,Donor_id,Donation_Date) values (13,NULL ,'O-',7,5,CURDATE());
insert into BLOOD (Blood_id,Special_Attributes,Blood_Group,Br_id,Donor_id,Donation_Date) values (14,NULL ,'A-',8,6,CURDATE());
insert into BLOOD (Blood_id,Special_Attributes,Blood_Group,Br_id,Donor_id,Donation_Date) values (15,NULL ,'B-', 7,7,CURDATE());
insert into BLOOD (Blood_id,Special_Attributes,Blood_Group,Br_id,Donor_id,Donation_Date) values (16,NULL ,'AB-', 8,8,CURDATE());
insert into BLOOD (Blood_id,Special_Attributes,Blood_Group,Br_id,Donor_id,Donation_Date) values (17,NULL ,'O+', 9,1,CURDATE());
insert into BLOOD (Blood_id,Special_Attributes,Blood_Group,Br_id,Donor_id,Donation_Date) values (18,NULL ,'A+', 9,2,CURDATE());
insert into BLOOD (Blood_id,Special_Attributes,Blood_Group,Br_id,Donor_id,Donation_Date) values (19,NULL ,'B+', 10,3,CURDATE());
insert into BLOOD (Blood_id,Special_Attributes,Blood_Group,Br_id,Donor_id,Donation_Date) values (20,NULL ,'AB+', 10,4,CURDATE());
insert into BLOOD (Blood_id,Special_Attributes,Blood_Group,Br_id,Donor_id,Donation_Date) values (21,NULL ,'O-', 11,5,CURDATE());
insert into BLOOD (Blood_id,Special_Attributes,Blood_Group,Br_id,Donor_id,Donation_Date) values (22,NULL ,'A-', 11,6,CURDATE());
insert into BLOOD (Blood_id,Special_Attributes,Blood_Group,Br_id,Donor_id,Donation_Date) values (23,NULL ,'AB-', 10,7,CURDATE());


insert into DONOR (Donor_id,Name,Blood_Group) values (1,'ascdsvds','O+');
insert into DONOR (Donor_id,Name,Blood_Group) values (2,'ascdsvds','A+');
insert into DONOR (Donor_id,Name,Blood_Group) values (3,'ascdsvds','B+');
insert into DONOR (Donor_id,Name,Blood_Group) values (4,'ascdsvds','AB+');
insert into DONOR (Donor_id,Name,Blood_Group) values (5,'ascdsvds','O-');
insert into DONOR (Donor_id,Name,Blood_Group) values (6,'ascdsvds','A-');
insert into DONOR (Donor_id,Name,Blood_Group) values (7,'ascdsvds','B-');
insert into DONOR (Donor_id,Name,Blood_Group) values (8,'ascdsvds','AB-');
