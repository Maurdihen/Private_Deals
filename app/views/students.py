from app.container import student_serv
from app.dao.model.student import StudentSchema

from flask_restx import Namespace, Resource
from flask import request


student_ns = Namespace("students")

student_schema = StudentSchema()
students_schema = StudentSchema(many=True)

@student_ns.route("/")
class StudentsView(Resource):
    """
    the link "/students/" has GET, POST requests
    """
    def get(self):
        """
        :return: dictionary list with data on all students
        """
        return students_schema.dump(student_serv.get_all()), 200

    def post(self):
        """
        :return: code 204, if a new entry in the DB was successfully made
        """
        data = request.json
        student_serv.create(data)
        return "", 201


@student_ns.route("/<int:fid>")
class StudentView(Resource):

    def get(self, fid):
        """
        :param fid: student's id
        :return: dictionary with data about one student by his identifier
        """
        return student_schema.dump(student_serv.get_one(fid)), 200

    def put(self, fid):
        """
        :return: code 204, if the new record in the database was successfully updated
        """
        data = request.json

        student_serv.update(data, fid)
        return "", 204

    def patch(self, fid):
        """
        :return: code 204, if the new record in the database was successfully updated
        """
        data = request.json

        student_serv.update_partial(data, fid)
        return "", 204

    def delete(self, fid):
        """
        :param fid: student's id
        :return: code 204, if the new record in the database was successfully delete
        """
        return student_serv.delete(fid), 204