from flask import Flask,request, jsonify
from bloodbank import Bloodbank
import json

app = Flask(__name__)

@app.route('/bloodbank', methods=['GET','POST','DELETE','PUT'])
def bloodbank_table():

    if request.method == 'GET':
        blood_bank_entry = request.get_json()
        #blood_bank_entry = json.loads(data)
        response = Bloodbank.get_bloodbank(blood_bank_entry)
        return jsonify(response)

    if request.method == 'POST':
        blood_bank_entry = request.get_json()
        #blood_bank_entry = json.loads(data)
        response = Bloodbank.insert_bloodbank(blood_bank_entry)
        return jsonify(response)
    #return jsonify({"status":400,"entry":"Incorrect Method call"})

    if request.method == 'PUT':
        blood_bank_entry = request.get_json()
        #blood_bank_entry = json.loads(data)
        response = Bloodbank.update_bloodbank(blood_bank_entry)
        return jsonify(response)
    #return jsonify({"status":400,"entry":"Incorrect Method call"})

    if request.method == 'DELETE':
        blood_bank_entry = request.get_json()
        #blood_bank_entry = json.loads(data)
        response = Bloodbank.delete_bloodbank(blood_bank_entry)
        return jsonify(response)
    #return jsonify({"status":400,"entry":"Incorrect Method call"})

    
    return jsonify({"status":400,"entry":"Incorrect Method call"})


if __name__ == '__main__':
    app.run(port=5000)