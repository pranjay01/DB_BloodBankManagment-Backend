#SJSU CMPE 138Spring2020 TEAM7

import mysql.connector as mysql
from connection import get_connection
from werkzeug.security import safe_str_cmp
from itsdangerous import URLSafeSerializer
from flask import request, jsonify, Response
from datetime import datetime
from itsdangerous.exc import BadSignature
#in seconds
session_time=3000

def login(admin_details):
    admin = Admin.find_by_email(admin_details["Email_id"])
    #passwrd = base64.b64encode(admin["Password"].encode("utf-8"))
    if admin and safe_str_cmp(admin["Password"], admin_details["Password"]):
        token = generate_token(admin["DBA_id"],admin_details["Email_id"])
        tmp = {"access_token":token}
        admin.update(tmp)
        return jsonify(admin)
    else:
        content = {
                    "description": "Email-id or password is wrong",
                    "error": "Access Forbidden",
                    "status_code": 403
                    }  
        response = jsonify(content)
        response.status_code=403
        return response


def generate_token(id,Email_id):    
    dt = datetime.today()  # Get timezone naive now
    seconds = dt.timestamp()
    expired_time = seconds + session_time

    s = URLSafeSerializer('project-blood-bank')
    token= s.dumps([seconds,id, Email_id,expired_time])
    return token

def authenticate_admin(request):
    head = request.headers.get('Authorization', None)
    
    if head:
        head1 = head.split()
        #head1 = head1[1]
        if len(head1)<2 or not head1:
            content = {
                        "description": "Request does not contain an access token",
                        "error": "Authorization Required",
                        "status_code": 401
                        }
            response = jsonify(content)
            response.status_code=401
            response.headers={'WWW-Authenticate': ' realm="Login Required"','Content-Type':'application/json'}
            return response
        s = URLSafeSerializer('project-blood-bank')
        try:
            values=s.loads(head1[1])
            admin = Admin.find_by_id(values[1])
            
            if admin["Email_id"]==values[2]:
                dt = datetime.today()  # Get timezone naive now
                currentseconds = dt.timestamp()
                if values[3]> currentseconds :
                    return 1
                else:
                    content={
                    "description": "Signature has expired",
                    "error": "Invalid token",
                    "status_code": 401
                    }
                    response = jsonify(content)
                    response.status_code=401
                    response.headers={'Content-Type':'application/json'}
                    return response
            else:
                content={
                "description": "Signature has expired",
                "error": "Invalid token",
                "status_code": 401
                }
                response = jsonify(content)
                response.status_code=401
                response.headers={'Content-Type':'application/json'}
                return response
        except BadSignature:
            content={
                    "description": "Invalid header string: Expecting value: line 1 column 1 (char 0)",
                    "error": "Invalid token",
                    "status_code": 401
                    }
            response = jsonify(content)
            response.status_code=401
            return response
       
    else:
        content = {
                    "description": "Request does not contain an access token",
                    "error": "Authorization Required",
                    "status_code": 401
                    }
        response = jsonify(content)
        response.status_code=401
        response.headers={'WWW-Authenticate': ' realm="Login Required"','Content-Type':'application/json'}
        return response



class Admin:
    def __init__(self,DBA_id,Email_id,Password):
        self.DBA_id =DBA_id
        self.Email_id =Email_id
        self.Password = Password

    @classmethod
    def find_by_email(self,email):
        db=get_connection()
        cursor = db.cursor()
        query = "SELECT * FROM DBA_LOGIN_CREDENTIALS WHERE Email_id=%s"
        try:
            cursor.execute(query,(email,))
            row = cursor.fetchone()
            if row:
                return {"DBA_id":row[0],"Email_id":row[1],"Password":row[2]}
            else:
                return None
        except mysql.Error as err:
            print("Internal Server error: {}".format(err))
            return {"status": 500, "message": str(err)}
        finally:
            db.close()

    @classmethod
    def find_by_id(self,_id):
        db=get_connection()
        cursor = db.cursor()
        query = "SELECT * FROM DBA_LOGIN_CREDENTIALS WHERE DBA_id=%s"
        try:
            cursor.execute(query,(_id,))
            row = cursor.fetchone()
            if row:
                return {"DBA_id":row[0],"Email_id":row[1],"Password":row[2]}
            else:
                return None
        except mysql.Error as err:
            print("Internal Server error: {}".format(err))
            return {"status": 500, "message": str(err)}
        finally:
            db.close()
