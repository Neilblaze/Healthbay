from ..models import db


class Patient(db.Model):
    __tablename__ = "patient"

    user_id = db.Column(db.Integer, db.ForeignKey("user.uid"), unique=True)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    height = db.Column(db.Float)
    weight = db.Column(db.Float)
    dob = db.Column(db.String(10))
    blood_group = db.Column(db.String(3))
    picture = db.String(db.String(100))
    contact = db.String(db.String(10))

    def __init__(
        self, name, height: float, weight: float, dob, blood_group, picture, contact
    ):
        self.name = name
        self.height = height
        self.weight = weight
        self.dob = dob
        self.blood_group = blood_group
        self.picture = picture
        self.contact = contact

    def __repr__(self):
        return f"<Patient(uid={self.name})>"

    @property
    def serialize(self):
        return {
            "name": self.name,
            "height": self.height,
            "weight": self.weight,
            "dob": self.dob,
            "blood_group": self.blood_group,
            "picture": self.picture,
            "contact": self.contact,
        }
