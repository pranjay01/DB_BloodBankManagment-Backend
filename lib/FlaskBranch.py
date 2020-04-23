#SJSU CMPE 138Spring2020 TEAM7

from flask import Flask,request, jsonify, json
from InsertBranch import InsertInTable, UpdateInTable, SelectInTable,DeleteInTable
import json
app = Flask(__name__)

@app.route('bloodbank/branch/add', methods=['GET','POST','DELETE','PUT'])
def add_donor():
    if request.method == 'POST':
        data = request.get_json()
        single_branch = json.loads(data)
        response = InsertInTable.branch(single_branch)
        return jsonify(response)
    return jsonify({"status":400,"entry":"Incorrect Method call"})

@app.route('bloodbank/branch/update',methods=['GET','POST','DELETE','PUT'])
def update_donor():
    if request.method == 'PUT':
        data = request.get_json()
        single_branch = json.loads(data)
        response = UpdateInTable.branch(single_branch)
        return jsonify(response)
    return jsonify({"status":400,"entry":"Incorrect Method call"})

@app.route('bloodbank/branch/delete',methods=['GET','POST','DELETE','PUT'])
def delete_donor():
    if request.method == 'DELETE':
        data = request.get_json()
        single_branch = json.loads(data)
        response = DeleteInTable.branch(single_branch)
        return jsonify(response)
    return jsonify({"status":400,"entry":"Incorrect Method call"})
    
@app.route('bloodbank/branch/',methods=['GET','POST','DELETE','PUT'])
def Index():
    if request.method == 'GET':
        data = request.get_json()
        single_branch = json.loads(data)
        response = SelectInTable.branch(single_branch)
        return jsonify(response)
    return jsonify({"status":400,"entry":"Incorrect Method call"})
if __name__ == '__main__':
  app.run(port=5000)