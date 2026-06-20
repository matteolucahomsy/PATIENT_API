from flask import Flask,jsonify
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
if __name__=="__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )