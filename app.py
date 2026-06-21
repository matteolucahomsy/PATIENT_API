from flask import Flask,jsonify,request
import sqlite3
app=Flask(__name__)
DATABASE= "patients.db"
def get_patient(code):
    conn=sqlite3.connect(DATABASE)
    conn.row_factory =sqlite3.Row
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM patients WHERE code=?",(code,))
    patient=cursor.fetchone()
    conn.close()
    return patient
@app.route("/patient",methods=["POST"])
def add_patient():
    data=request.get_json()
    conn=sqlite3.connect(DATABASE)
    cursor=conn.cursor()
    cursor.execute("INSERT INTO patients(code,name,illness,medication,schedule,notes) VALUES (?,?,?,?,?,?)",(data["code"],data["name"],data["illness"],data["medication"],data["schedule"],data["notes"]))
    conn.commit()
    conn.close()
    return jsonify ({
        "message" : "Patient added successfully"
    }),201
@app.route("/patient/<code>")
def patient(code):
    p=get_patient(code)
    if p is None:
        return jsonify({
            "error": "Patient not found"
        }), 404
    return jsonify({
        "code": p["code"],
        "name": p["name"],
        "illness": p["illness"],
        "medication": p["medication"],
        "schedule": p["schedule"],
        "notes": p["notes"]
    })
@app.route("/patient/<code>", methods=["DELETE"])
def delte_patient(code):
    print("Delte called for: ",code)
    conn=sqlite3.connect(DATABASE)
    cursor=conn.cursor()
    cursor.execute("DELETE FROM patients WHERE code=?",(code,))
    conn.commit()
    conn.close()
    return jsonify({
        "message":f"Patient {code} deleted"
    })
@app.route("/patient/<code>", methods=["PUT"])
def update_patient(code):
    data=request.get_json()
    conn=sqlite3.connect(DATABASE)
    cursor=conn.cursor()
    cursor.execute("UPDATE patients SET name=?,illness=?,medication=?,schedule=?,notes=? WHERE code=?",(data["name"],data["illness"],data["medication"],data["schedule"],data["notes"],code))
    conn.commit()
    conn.close()
    return jsonify ({
        "message" : f"Patient {code} updated"
    })
if __name__=="__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )