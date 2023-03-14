from marshmallow import Schema, fields
from app.setup_db import db


class Mother(db.Model):
    __tablename__ = 'mother'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    surname = db.Column(db.String, nullable=True)
    patronymic = db.Column(db.String, nullable=True)
    number = db.Column(db.String, nullable=True)
    job = db.Column(db.String, nullable=True)


class MotherSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    surname = fields.String()
    patronymic = fields.String()
    number = fields.String()
    job = fields.String()
