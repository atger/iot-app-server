import json
from datetime import date, datetime
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)

@app.route('/api/bin_level', methods=['POST'])
@cross_origin(supports_credentials=True)
def setBinLevel():
    args = request.args
    print([request.args, request.form])
    json_object = json.dumps(request.form, indent=4)
    with open("bin_level.json", "w") as f:
        f.write(json_object)
    return json_object

@app.route('/api/level', methods=['GET'])
@cross_origin(supports_credentials=True)
def getBinLevel():
    level = "0"
    with open("bin_level.json") as f:
        json_object = json.load(f)
        if "level" in json_object:
            level = json_object.get("level")
    return level

@app.route('/api/attendance', methods=['POST'])
@cross_origin(supports_credentials=True)
def storeAttendance():
    name = request.form.get("name")
    date_time = datetime.now()
    args = { "date": date_time.strftime("%d-%m-%y"), 
            "time": date_time.strftime("%H:%M %p"),
            "name": name }
    print([request.args, request.form])
    with open("attendance_data.json") as f:
        attendance_dict = json.load(f)
        attendance_dict["data"].append(args)
        with open("attendance_data.json", "w") as g:
            json.dump(attendance_dict, g)
    return json.dumps(args, indent=4)

@app.route('/api/attendance', methods=['GET'])
@cross_origin(supports_credentials=True)
def retrieveAttendance():
    with open("attendance_data.json") as f:
        json_object = json.load(f)
    return json_object["data"]

@app.route('/api/attendance/clear', methods=['DELETE'])
@cross_origin(supports_credentials=True)
def clearAttendance():
    with open("attendance_data.json") as f:
        attendance_dict = json.load(f)
        attendance_dict["data"] = []
        with open("attendance_data.json", "w") as g:
            json.dump(attendance_dict, g)
    return "", 200





if __name__ == "__main__":
    app.run(host='0.0.0.0')
