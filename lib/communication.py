#SJSU CMPE 138Spring2020 TEAM7

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import mysql.connector as mysql
from connection import get_connection

#Sender email
email = "bloodbankmanagement2020@gmail.com"
password = "Team7@2020"
# email = "cmpe272project2020@gmail.com"
# password = "CMPE@272"
bld_grp=('O+','A+','B+','AB+','O-','A-','B-','AB-')
#reciever number and email address
#sms_gateway = '5855246544@tmomail.net'  #tmomail.net is used for tmobile numbers
#receiver_email = "pranjay.sagar@sjsu.edu"

# Using smtp server we use is gmail smtp server ( the port comes by default with the gmail server)
smtp = "smtp.gmail.com" 
port = 587

#what we want the body and subject contents to be
subject_content="Urgent Blood Needed\n"
#body_content="Gunshot sound heard, Need assistance!!\n"


#login
def send_notification(operator_id,params):
    get_phone_list = "select Phone_no from DONOR_PHONE as dp join DONOR as dn on \
                    (dp.Donor_id=dn.Donor_id) where Notification_Subscription=true \
                        and Notification_Type=%s and Blood_Group=%s and dn.Donor_id  \
                        in (select Donor_id from AFFILIATED where Operator_id=%s)"
                        
    get_email_list = "select Email_id from DONOR_EMAIL as dp join DONOR as dn on \
                    (dp.Donor_id=dn.Donor_id) where Notification_Subscription=true \
                        and Notification_Type=%s and Blood_Group=%s and dn.Donor_id  \
                        in (select Donor_id from AFFILIATED where Operator_id=%s)"     

    
    try:
        db=get_connection()
        cursor = db.cursor()
        cursor.execute(get_phone_list,(2,int(params["Blood_Group"]),int(operator_id)))
        result = cursor.fetchall()
        phone_list=[]
        for phone in result:
            phone_list.append(str(phone[0])+'@tmomail.net')

        cursor.execute(get_email_list,(1,int(params["Blood_Group"]),int(operator_id)))
        result = cursor.fetchall()
        email_list=[]
        for email in result:
            email_list.append(email[0])
        
        bankname="SELECT Name from BLOOD_BANK where Bbank_id=%s"
        cursor.execute(bankname,(int(params["Bbank_id"]),))
        row = cursor.fetchone()

        body = params["body"] + "\n" + "Required Blood Group: " + bld_grp[int(params["Blood_Group"])-1] +"ve. "

        # server = smtplib.SMTP(smtp,port)
        # server.starttls()
        # server.login(email,password)
        if email_list:        
            send_email(email_list,row[0],body)
        if phone_list:
            send_msg(phone_list,row[0],body)
        # server.quit()
        if (not email_list) and (not phone_list):
            return {"status":200, "message":"No donor found for sending notification"}    
        return {"status":200, "message":"Notification Sent"}
    except mysql.Error as err:
            print("Internal Server error: {}".format(err))
            return {"status": 500, "message": str(err)}
    finally:
        db.close()


#To send sms text message
def send_msg(reciepients,sender_bank_name,body_content):
    server = smtplib.SMTP(smtp,port)
    server.starttls()
    server.login(email,password)

    #sms_gateway = str(modileNo) + '@tmomail.net'
    for reciever in reciepients:
        textmsg = MIMEMultipart()
        textmsg['From'] = sender_bank_name
        textmsg['To'] = reciever
        textmsg['Subject'] = subject_content
        body = body_content
        textmsg.attach(MIMEText(body, 'plain'))
        sms = textmsg.as_string()
        server.sendmail(email,reciever,sms)
    server.quit()

# Send Email
def send_email(reciepients,sender_bank_name,body_content):
    #starts pythons email server
    server = smtplib.SMTP(smtp,port)
    server.starttls()
    server.login(email,password)
    for reciever in reciepients:
        emailMessage = MIMEMultipart()
        emailMessage['From'] = sender_bank_name
        emailMessage['To'] = reciever
        emailMessage['Subject'] = subject_content
        body = body_content
        emailMessage.attach(MIMEText(body, 'plain'))
        mailAlert = emailMessage.as_string()
        server.sendmail(email,reciever,mailAlert)
    server.quit()
    



