from flask import Flask,request, jsonify
from InsertDonor import InsertInTable, UpdateInTable, SelectInTable,DeleteInTable
import json
app = Flask(__name__)


@app.route('bloodbank/donor/add', methods=['GET','POST','DELETE','PUT'])
def add_donor():
    if request.method == 'POST':
        data = request.get_json()
        single_donor = json.loads(data)
        response = InsertInTable.donor(single_donor)
        return jsonify(response)
    return jsonify({"status":400,"entry":"Incorrect Method call"})


@app.route('bloodbank/donor/update',methods=['GET','POST','DELETE','PUT'])
def update_donor():
    if request.method == 'PUT':
        data = request.get_json()
        single_donor = json.loads(data)
        response = UpdateInTable.donor(single_donor)
        return jsonify(response)
    return jsonify({"status":400,"entry":"Incorrect Method call"})


@app.route('bloodbank/donor/delete',methods=['GET','POST','DELETE','PUT'])
def delete_donor():
    if request.method == 'DELETE':
        data = request.get_json()
        single_donor = json.loads(data)
        response = DeleteInTable.donor(single_donor)
        return jsonify(response)
    return jsonify({"status":400,"entry":"Incorrect Method call"})


@app.route('bloodbank/donor',methods=['GET','POST','DELETE','PUT'])
def select_donor():
    if request.method == 'GET':
        data = request.get_json()
        single_donor = json.loads(data)
        response = SelectInTable.donor(single_donor)
        return jsonify(response)
    return jsonify({"status":400,"entry":"Incorrect Method call"})


@app.route('bloodbank/donor/econtact',methods=['GET','POST','DELETE','PUT'])
def add_contact():
    if request.method == 'POST':
        data = request.get_json()
        single_donor = json.loads(data)
        response = InsertInTable.donor_contact(single_donor)
        return jsonify(response)
    return jsonify({"status":400,"entry":"Incorrect Method call"})


@app.route('bloodbank/donor/econtact/update',methods=['GET','POST','DELETE','PUT'])
def update_contact():
    if request.method == 'PUT':
        data = request.get_json()
        single_donor = json.loads(data)
        response = UpdateInTable.donor(single_donor)
        return jsonify(response)
    return jsonify({"status":400,"entry":"Incorrect Method call"})


@app.route('bloodbank/donor/econtact/delete',methods=['GET','POST','DELETE','PUT'])
def delete_contact():
    if request.method == 'DELETE':
        data = request.get_json()
        single_donor = json.loads(data)
        response = DeleteInTable.donor(single_donor)
        return jsonify(response)
    return jsonify({"status":400,"entry":"Incorrect Method call"})


@app.route('bloodbank/donor/econtact',methods=['GET','POST','DELETE','PUT'])
def select_contact():
    if request.method == 'GET':
        data = request.get_json()
        single_donor = json.loads(data)
        response = SelectInTable.donor(single_donor)
        return jsonify(response)
    return jsonify({"status":400,"entry":"Incorrect Method call"})


if __name__ == '__main__':
  app.run(port=5000)