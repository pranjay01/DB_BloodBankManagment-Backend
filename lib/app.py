from flask import Flask,request, jsonify
from blood import Blood, BloodStock
import json
from flask_jwt import JWT, jwt_required
from security import authenticate, identity
from user import Operator
from datetime import timedelta

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

@app.route('/<Operator_id>/signup', methods=['POST'])
#API to create ne operator
def create_operator():
  new_operator=request.get_json()
  #new_operator = json.loads(data)
  if Operator.find_by_email(new_operator['Email']):
    return {"message":"A user with same name already exists"}, 400
  else:
    Operator.register(new_operator)



#Operations by Operator related to blood and blood_stock table 

@app.route('/<Operator_id>/blood', methods=['GET','POST','DELETE','PUT'])

#API function to insert new blood unit from donor
#Required compulsory info, donor id, branch id
@jwt_required()
def add_blood_unit(Operator_id):
  
  if request.method == 'POST':
    bloodUnit=request.get_json()
    #bloodUnit = json.loads(data)
    response = Blood.insert_blood(bloodUnit,Operator_id)
    return jsonify(response)
  return jsonify({"status":400,"message":"Incorrect Method call"})

@jwt_required()
def return_blood_unit(Operator_id):
  #API function to get blood unit information on one of the following basis
  #Case 1: list branch wise blood unit count required Bbank_id
  #Case 2: list blood group wise blood unit count of that particular branch : required branch id
  #case 3: list all blood units info of a particular branch and blood group : required branchid and blood group
  if request.method == 'GET':
    parameters = request.get_json()
    #parameters = json.loads(data)
    response = Blood.get_blood_units(parameters,Operator_id)
    return jsonify(response)
  return jsonify({"status":400,"message":"Incorrect Method call"})


@jwt_required()
def update_blood_unit_info(Operator_id):
  #API function to update blood unit information in 2 cases
  #Case 1:Only Special attributes is updated. :required blood _id, special attributes value to update
  #when 2:When transferring blood units from current branch to other branch, required 3 parameters
  #1-target branch, 2-count of blood units to be transferred, 3-blood group
  if request.method == 'PUT':
    parameters = request.get_json()
    #parameters = json.loads(data)
    response = Blood.upadate_blood_bank(parameters,Operator_id)
    return jsonify(response)
  return jsonify({"status":400,"message":"Incorrect Method call"})


@jwt_required()
def delete_blood_unit(Operator_id):
  #API function to delete blood unit 
  #Required parameter only blood id
  if request.method == 'DELETE':
    bloodUnit = request.get_json()
    #bloodUnit = json.loads(data)
    response = Blood.delete_blood_unit(bloodUnit,Operator_id)
    return jsonify(response)
  return jsonify({"status":400,"message":"Incorrect Method call"})


#API to update the minimum limit of a particular blood goup 
#in one of the operators corresponding branch
@jwt_required()
@app.route('/<Operator_id>/blood_limt', methods=['PUT'])
def update_limit(Operator_id):
  parameters = request.get_json()
  #parameters = json.loads(data)
  response = BloodStock.update_blood_stock_limit(parameters,Operator_id)
  return jsonify(response)


#API for the guest user to check the availability of bloodunits in different blood banks
#accross the city
@app.route('/guest_user/blood', methods=['GET'])
def get_blood_unit_count_for_user():
  parameters = request.get_json()
  #parameters = json.loads(data)
  response = Blood.get_bloodunit_list_guest_user(parameters)
  return jsonify(response)


@jwt_required()
@app.route('/<Operator_id>/expired_blood', methods=['GET','DELETE'])
def get_expired_bloodUnits(Operator_id):
  #return all the expired blood units of the blood bank of which operator belongs to
  if request.method == 'GET':      
    parameters = request.get_json()
    #parameters = json.loads(data)
    response = Blood.get_expired_units(parameters,Operator_id)
    return jsonify(response)
  return jsonify({"status":400,"message":"Incorrect Method call"})

@jwt_required()
def delete_expired_bloodUnits(Operator_id):
  #delete all the expired blood units of that particular blood bank
  if request.method == 'DELETE':      
    parameters = request.get_json()
    #parameters = json.loads(data)
    response = Blood.delete_expired_units(parameters,Operator_id)
    return jsonify(response)
  return jsonify({"status":400,"message":"Incorrect Method call"})



if __name__ == '__main__':
  app.run(port=5000)