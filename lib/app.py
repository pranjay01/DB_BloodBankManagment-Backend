from flask import Flask,request, jsonify
from blood import Blood


app = Flask(__name__)



@app.route('/blood', methods=['GET','POST','DELETE','PUT'])
def blood_table():
  if request.method == 'POST':

    data=request.get_json()
    bloodUnit={
        "spcl_attr" : data['spcl_attr'],
        "bl_grp"    : data['bl_grp'],
	      "br_id"     : data['br_id'],
	      "dnr_id"    : data['dnr_id'],
        
    }
    Blood.insert_blood(bloodUnit)


  return jsonify({"blood_unit":bloodUnit})

if __name__ == '__main__':
  app.run(port=5000)