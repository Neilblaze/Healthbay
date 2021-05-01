from flask import request, jsonify, make_response

from ... import db
from ...middleware.firebase_auth import token_required
from ...routes import api as app
from ...models.doctor import Doctor


@app.route("/onboarding/doctor", methods=["POST"])
@token_required
def create_doctor(current_user):
    name, height, weight = (
        request.form["name"],
        float(request.form["height"]),
        float(request.form["weight"]),
    )
    dob, blood_group, picture = (
        request.form["dob"],
        request.form["blood_group"],
        request.form["picture"],
    )
    contact = request.form["contact"]

    patient_obj = Doctor("#TODO")
    patient_obj.user_id = current_user.uid
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