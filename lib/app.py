from flask import Flask,request, jsonify
from blood import Blood, BloodStock
import json
<<<<<<< HEAD

=======
from flask_jwt import JWT, jwt_required
from security import authenticate, identity
from user import Operator
from datetime import timedelta
>>>>>>> b7cc422944a25f3e8e079a1a2706535d792042bc

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dbProject'
app.config['JWT_AUTH_URL_RULE'] = '/operator_login'
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=3000)
app.config['JWT_AUTH_USERNAME_KEY'] = 'Email'
app.config['JWT_AUTH_PASSWORD_KEY'] = 'Password'


jwt = JWT(app, authenticate, identity)

#Operator login and authentication token generation
@jwt.auth_response_handler
def customized_response_handler(access_token, identity):

  return jsonify({
                  'access_token': access_token.decode('utf-8'),
                  'Operator_id': identity.id
                   })


#  @jwt.error_handler
#  def customized_error_handler(error):
#    return jsonify({
#                        'message': error.description,
#                        'code': error.status_code
#                    }), error.status_code

@app.route('/operator/blood', methods=['GET','POST','DELETE','PUT'])

#API function to insert new blood unit from donor
#Required compulsory info, donor id, branch id
def add_blood_unit():
  
  if request.method == 'POST':
    data=request.get_json()
    bloodUnit = json.loads(data)
    response = Blood.insert_blood(bloodUnit)
    return jsonify(response)
  return jsonify({"status":400,"entry":"Incorrect Method call"})

def return_blood_unit():
  #API function to get blood unit information on one of the following basis
  #Case 1: list branch wise blood unit count : required blood bank id
  #Case 2: list blood group wise blood unit count of that particular branch : required branch id
  #case 3: list all blood units info of a particular branch and blood group : required branchid and blood group
  if request.method == 'GET':
    data = request.get_json()
    parameters = json.loads(data)
    response = Blood.get_blood_units(parameters)
    return jsonify(response)
  return jsonify({"status":400,"entry":"Incorrect Method call"})


def update_blood_unit_info():
  #API function to update blood unit information in 2 cases
  #Case 1:Only Special attributes is updated. :required blood _id, special attributes value to update
  #when 2:When transferring blood units from current branch to other branch, required 3 parameters
  #1-target branch, 2-count of blood units to be transferred, 3-blood group
  if request.method == 'PUT':
    data = request.get_json()
    parameters = json.loads(data)
    response = Blood.upadate_blood_bank(parameters)
    return jsonify(response)
  return jsonify({"status":400,"entry":"Incorrect Method call"})


def delete_blood_unit():
  #API function to delete blood unit 
  #Required parameter only blood id
  if request.method == 'DELETE':
    data = request.get_json()
    bloodUnit = json.loads(data)
    response = Blood.get_blood_units(bloodUnit)
    return jsonify(response)
  return jsonify({"status":400,"entry":"Incorrect Method call"})


@app.route('/operator/blood_limt', methods=['PUT'])
def update_limit():
  data = request.get_json()
  parameters = json.loads(data)
  response = BloodStock.update_blood_stock_limit(parameters)
  return jsonify(response)


@app.route('/user/blood', methods=['GET'])
def get_blood_unit_count_for_user():
  data = request.get_json()
  parameters = json.loads(data)
  response = Blood.get_bloodunit_list_guest_user(parameters)
  return jsonify(response)


@app.route('/operator/expired_blood', methods=['GET','DELETE'])
def get_expired_bloodUnits():
  #return all the expired blood units of the blood bank of which operator belongs to
  if request.method == 'GET':      
    data = request.get_json()
    parameters = json.loads(data)
    response = Blood.get_expired_units(parameters)
    return jsonify(response)
  return jsonify({"status":400,"entry":"Incorrect Method call"})

def delete_expired_bloodUnits():
  if request.method == 'DELETE':      
    data = request.get_json()
    parameters = json.loads(data)
    response = Blood.delete_expired_units(parameters)
    return jsonify(response)
  return jsonify({"status":400,"entry":"Incorrect Method call"})



if __name__ == '__main__':
  app.run(port=5000)