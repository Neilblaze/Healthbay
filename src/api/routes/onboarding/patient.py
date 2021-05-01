from flask import request, jsonify, make_response

from api import app

from ...models import db
from ...models.patient import Patient


@app.route("/user", methods=["POST"])
def create_user():
    name, height, weight = (
        request.form["name"],
        float(request.form["height"]),
        float(request.form["weight"]),
    )
    dob, blood_group, picture = (
        request.form["dob"],
        request.form["blood_group"],
        request.files["picture"],
    )
    contact = request.form["contact"]

    patient_obj = Patient(name, height, weight, dob, blood_group, picture, contact)
    db.session.add(patient_obj)
    db.session.commit()

    return make_response(
        jsonify(
            {
                "status": "OK",
                "message": "Successfully onboarded patient",
            }
        ),
        200,
    )