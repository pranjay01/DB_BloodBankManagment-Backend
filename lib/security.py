#SJSU CMPE 138Spring2020 TEAM7

from werkzeug.security import safe_str_cmp
from user import Operator
import base64


def authenticate(email, password):
    operator = Operator.find_by_email(email)
    passwrd = base64.b64encode(password.encode("utf-8"))
    if operator and safe_str_cmp(operator.Password, passwrd):
        return operator

def identity(payload):
    user_id = payload['identity']
    return Operator.find_by_id(user_id)