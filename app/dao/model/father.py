from marshmallow import Schema, fields
from app.setup_db import db


class Father(db.Model):
    __tablename__ = 'father'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    surname = db.Column(db.String, nullable=True)
    patronymic = db.Column(db.Integer, nullable=True)
    number = db.Column(db.String, nullable=True)
    job = db.Column(db.String, nullable=True)


class FatherSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    surname = fields.String()
    patronymic = fields.Integer()
    number = fields.String()
    job = fields.String()
