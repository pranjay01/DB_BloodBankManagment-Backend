from flask import Flask,request, jsonify
from blood import Blood, BloodStock
import json
from flask_jwt import JWT, jwt_required
from security import authenticate, identity
from user import Operator
from datetime import timedelta
from bloodbank import Bloodbank
from InsertDonor import InsertInTable, UpdateInTable, SelectInTable,DeleteInTable
from operator import Operators, Blood_donation_event


app = Flask(__name__)
app.config['SECRET_KEY'] = 'dbProject'
app.config['JWT_AUTH_URL_RULE'] = '/operator_login'
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=3000)
app.config['JWT_AUTH_USERNAME_KEY'] = 'Email'
app.config['JWT_AUTH_PASSWORD_KEY'] = 'Password'


############## LOGIN/SIGNUP APIs #############################################
#
####################################################################################

jwt = JWT(app, authenticate, identity)

#Operator login and authentication token generation
@jwt.auth_response_handler
def customized_response_handler(access_token, identity):

  return jsonify({
                  'access_token': access_token.decode('utf-8'),
                  'Operator_id': identity.id,
                  'Name': identity.Name,
                  'Bbank_id': identity.Bbank_id,
                  'method': 'POST',
                  'status': 200
                   })


#SIGNUP for Operator
@app.route('/operator/signup', methods=['POST'])
#API to create ne operator
def create_operator():
  new_operator=request.get_json()
  #new_operator = json.loads(data)
  if Operator.find_by_email(new_operator['Email']):
    return jsonify({"status":400,"message":"A user with same name already exists"})
  else:
    response= Operator.register(new_operator)
    return jsonify(response)

############## BLOOD-Bank RELATED APIs #############################################
#
####################################################################################

@app.route('/bloodbank', methods=['GET','POST','DELETE','PUT'])
def bloodbank_table():
  #have 2 cases, both case api calls being done by Admin
  # case 1: give list of all blood banks
  # case 2: give information of only 1 particular blood bank 
  if request.method == 'GET':
        blood_bank_entry = request.args
        response = Bloodbank.get_bloodbank(blood_bank_entry)
        return jsonify(response)

  # accessible by only admin
  if request.method == 'POST':
        blood_bank_entry = request.get_json()
        response = Bloodbank.insert_bloodbank(blood_bank_entry)
        return jsonify(response)

  if request.method == 'PUT':
        blood_bank_entry = request.get_json()
        response = Bloodbank.update_bloodbank(blood_bank_entry)
        return jsonify(response)

  if request.method == 'DELETE':
        blood_bank_entry = request.get_json()
        response = Bloodbank.delete_bloodbank(blood_bank_entry)
        return jsonify(response)
  return jsonify({"status":400,"entry":"Incorrect Method call"})



############## BLOOD RELATED APIs #############################################
#Operations by Operator related to blood and blood_stock table 
###############################################################################


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

#@jwt_required()
#def return_blood_unit(Operator_id):
  #API function to get blood unit information on one of the following basis
  #Case 1: Get total blood unit for the blood bank associated to the operator
  #Case 2: list branch wise blood unit count required Bbank_id
  #Case 3: list blood group wise blood unit count of that particular branch : required branch id
  #case 4: list all blood units info of a particular branch and blood group : required branchid and blood group
  if request.method == 'GET':
    parameters = request.args
    #parameters = json.loads(data)
    response = Blood.get_blood_units(parameters,Operator_id)
    return jsonify(response)


#@jwt_required()
#def update_blood_unit_info(Operator_id):
  #API function to update blood unit information in 2 cases
  #Case 1:Only Special attributes is updated. :required blood _id, special attributes value to update
  #when 2:When transferring blood units from current branch to other branch, required 3 parameters
  #1-target branch, 2-count of blood units to be transferred, 3-blood group
  if request.method == 'PUT':
    parameters = request.get_json()
    #parameters = json.loads(data)
    response = Blood.upadate_blood_bank(parameters,Operator_id)
    return jsonify(response)


##def delete_blood_unit(Operator_id):
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

@jwt_required()
@app.route('/<Operator_id>/expired_blood', methods=['GET','DELETE'])
def get_expired_bloodUnits(Operator_id):
  #return all the expired blood units of the blood bank of which operator belongs to
  if request.method == 'GET':      
    parameters = request.args
    #parameters = json.loads(data)
    response = Blood.get_expired_units(parameters,Operator_id)
    return jsonify(response)

#@jwt_required()
#def delete_expired_bloodUnits(Operator_id):
  #delete all the expired blood units of that particular blood bank
  if request.method == 'DELETE':      
    parameters = request.get_json()
    #parameters = json.loads(data)
    response = Blood.delete_expired_units(parameters,Operator_id)
    return jsonify(response)
  return jsonify({"status":400,"message":"Incorrect Method call"})



################################################################################

#API for the guest user to check the availability of bloodunits in
#different blood banks accross the city

################################################################################
@app.route('/guest_user/blood', methods=['GET'])
def get_blood_unit_count_for_user():
  parameters = request.args
  #parameters = json.loads(data)
  response = Blood.get_bloodunit_list_guest_user(parameters)
  return jsonify(response)


############  APIs for Donor related ##########################################


################################################################################

@app.route('/bloodbank/donor/add', methods=['GET','POST','DELETE','PUT'])
@jwt_required
def add_donor():
    if request.method == 'POST':
        data = request.get_json()
        single_donor = json.loads(data)
        response = InsertInTable.donor(single_donor)
        return jsonify(response)
    return jsonify({"status":400,"entry":"Incorrect Method call"})

@jwt_required
@app.route('/bloodbank/donor/update',methods=['GET','POST','DELETE','PUT'])
def update_donor():
    if request.method == 'PUT':
        data = request.get_json()
        single_donor = json.loads(data)
        response = UpdateInTable.donor(single_donor)
        return jsonify(response)
    return jsonify({"status":400,"entry":"Incorrect Method call"})

@jwt_required
@app.route('/bloodbank/donor/delete',methods=['GET','POST','DELETE','PUT'])
def delete_donor():
    if request.method == 'DELETE':
        data = request.get_json()
        single_donor = json.loads(data)
        response = DeleteInTable.donor(single_donor)
        return jsonify(response)
    return jsonify({"status":400,"entry":"Incorrect Method call"})


@app.route('/bloodbank/donor',methods=['GET','POST','DELETE','PUT'])
def select_donor():
    if request.method == 'GET':
        #data = request.get_json()
        single_donor = request.args
        response = SelectInTable.donor(single_donor)
        return jsonify(response)
    return jsonify({"status":400,"entry":"Incorrect Method call"})

@jwt_required
@app.route('/bloodbank/donor/econtact',methods=['GET','POST','DELETE','PUT'])
def add_contact():
    if request.method == 'POST':
        data = request.get_json()
        single_donor = json.loads(data)
        response = InsertInTable.donor_contact(single_donor)
        return jsonify(response)
    return jsonify({"status":400,"entry":"Incorrect Method call"})

@jwt_required
@app.route('/bloodbank/donor/econtact/update',methods=['GET','POST','DELETE','PUT'])
def update_contact():
    if request.method == 'PUT':
        data = request.get_json()
        single_donor = json.loads(data)
        response = UpdateInTable.donor(single_donor)
        return jsonify(response)
    return jsonify({"status":400,"entry":"Incorrect Method call"})

@jwt_required
@app.route('/bloodbank/donor/econtact/delete',methods=['GET','POST','DELETE','PUT'])
def delete_contact():
    if request.method == 'DELETE':
        data = request.get_json()
        single_donor = json.loads(data)
        response = DeleteInTable.donor(single_donor)
        return jsonify(response)
    return jsonify({"status":400,"entry":"Incorrect Method call"})


@app.route('/bloodbank/donor/econtact',methods=['GET','POST','DELETE','PUT'])
def select_contact():
    if request.method == 'GET':
        data = request.args
        single_donor = json.loads(data)
        response = SelectInTable.donor(single_donor)
        return jsonify(response)
    return jsonify({"status":400,"entry":"Incorrect Method call"})


############  APIs for Operator related Table###################################


################################################################################

@app.route('/operator', methods=['GET', 'DELETE', 'PUT'])
def operator_table():

  #Get list of all operators
  if request.method == 'GET':
      operator_entry = request.get_json()
      response = Operators.get_operator(operator_entry)
      return jsonify(response)

  if request.method == 'PUT':
      operator_entry = request.get_json()
      response = Operators.update_operator(operator_entry)
      return jsonify(response)
  # return jsonify({"status":400,"entry":"Incorrect Method call"})

  if request.method == 'DELETE':
      operator_entry = request.get_json()
      response = Operators.delete_operator(operator_entry)
      return jsonify(response)
      # return jsonify({"status":400,"entry":"Incorrect Method call"})

  return jsonify({"status": 400, "entry": "Incorrect Method call"})




############  APIs for Blood DOnation related Table###################################


################################################################################


@app.route('/blood_donation_event', methods=['GET', 'POST', 'DELETE', 'PUT'])
def blood_donation_event_table():

  if request.method == 'GET':
      blood_donation_event_entry = request.get_json()
      # blood_donation_event_entry = json.loads(data)
      response = Blood_donation_event.get_blood_donation_event(blood_donation_event_entry)
      return jsonify(response)

  if request.method == 'POST':
      blood_donation_event_entry = request.get_json()
      # blood_donation_event_entry = json.loads(data)
      response = Blood_donation_event.insert_blood_donation_event(blood_donation_event_entry)
      return jsonify(response)
  # return jsonify({"status":400,"entry":"Incorrect Method call"})

  if request.method == 'PUT':
      blood_donation_event_entry = request.get_json()
      # blood_donation_event_entry = json.loads(data)
      response = Blood_donation_event.update_blood_donation_event(blood_donation_event_entry)
      return jsonify(response)
  # return jsonify({"status":400,"entry":"Incorrect Method call"})

  if request.method == 'DELETE':
      blood_donation_event_entry = request.get_json()
      event = request.get_json()
      response = Blood_donation_event.delete_blood_donation_event(event)
      return jsonify(response)
  # return jsonify({"status":400,"entry":"Incorrect Method call"})

  return jsonify({"status": 400, "entry": "Incorrect Method call"})

@app.route('/<operator_id>/blood_donation_event/all', methods=['GET', 'POST', 'DELETE', 'PUT'])
def list_all_event_list_of_operator(operator_id):
  response = Blood_donation_event.get_operator_vent_list(operator_id)
  return jsonify(response)


if __name__ == '__main__':
  app.run(port=5000)