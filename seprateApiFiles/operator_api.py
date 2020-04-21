from flask import Flask, request, jsonify
#from operator import Operator
import json

app = Flask(__name__)


@app.route('/operator', methods=['GET', 'POST', 'DELETE', 'PUT'])
def operator_table():
    if request.method == 'GET':
        operator_entry = request.get_json()
        # operator_entry = json.loads(data)
        response = Operator.get_operator(operator_entry)
        return jsonify(response)

    if request.method == 'POST':
        operator_entry = request.get_json()
        # operator_entry = json.loads(data)
        response = Operator.insert_operator(operator_entry)
        return jsonify(response)
    # return jsonify({"status":400,"entry":"Incorrect Method call"})

    if request.method == 'PUT':
        operator_entry = request.get_json()
        # operator_entry = json.loads(data)
        response = Operator.update_operator(operator_entry)
        return jsonify(response)
    # return jsonify({"status":400,"entry":"Incorrect Method call"})

    if request.method == 'DELETE':
        operator_entry = request.get_json()
        # operator_entry = json.loads(data)
        response = Operator.delete_operator(operator_entry)
        return jsonify(response)
       # return jsonify({"status":400,"entry":"Incorrect Method call"})

    return jsonify({"status": 400, "entry": "Incorrect Method call"})


@app.route('/blood_donation_event', methods=['GET', 'POST', 'DELETE', 'PUT'])
def blood_donation_event_table():
    if request.method == 'GET':
        blood_donation_event_entry = request.get_json()
        # blood_donation_event_entry = json.loads(data)
        #response = Blood_donation_event.get_blood_donation_event(blood_donation_event_entry)
        return jsonify(response)

    if request.method == 'POST':
        blood_donation_event_entry = request.get_json()
        # blood_donation_event_entry = json.loads(data)
        #response = Blood_donation_event.insert_blood_donation_event(blood_donation_event_entry)
        return jsonify(response)
    # return jsonify({"status":400,"entry":"Incorrect Method call"})

    if request.method == 'PUT':
        blood_donation_event_entry = request.get_json()
        # blood_donation_event_entry = json.loads(data)
        #response = Blood_donation_event.update_blood_donation_event(blood_donation_event_entry)
        return jsonify(response)
    # return jsonify({"status":400,"entry":"Incorrect Method call"})

    if request.method == 'DELETE':
        blood_donation_event_entry = request.get_json()
        # operator_entry = json.loads(data)
        #response = Blood_donation_event.delete_blood_donation_event(operator_blood_donation_event)
        return jsonify(response)
    # return jsonify({"status":400,"entry":"Incorrect Method call"})

    return jsonify({"status": 400, "entry": "Incorrect Method call"})





if __name__ == '__main__':
    app.run(port=5000)
