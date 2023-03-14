from app.container import mother_serv
from app.dao.model.mother import MotherSchema

from flask_restx import Namespace, Resource
from flask import request


mother_ns = Namespace("mothers")

mother_schema = MotherSchema()
mothers_schema = MotherSchema(many=True)

@mother_ns.route("/")
class MothersView(Resource):
    """
    the link "/mothers/" has GET, POST requests
    """
    def get(self):
        """
        :return: dictionary list with data on all mothers
        """
        return mothers_schema.dump(mother_serv.get_all()), 200

    def post(self):
        """
        :return: code 204, if a new entry in the DB was successfully made
        """
        data = request.json
        mother_serv.create(data)
        return "", 201


@mother_ns.route("/<int:fid>")
class MotherView(Resource):

    def get(self, fid):
        """
        :param fid: mother's id
        :return: dictionary with data about one mother by his identifier
        """
        return mother_schema.dump(mother_serv.get_one(fid)), 200

    def put(self, fid):
        """
        :return: code 204, if the new record in the database was successfully updated
        """
        data = request.json

        mother_serv.update(data, fid)
        return "", 204

    def patch(self, fid):
        """
        :return: code 204, if the new record in the database was successfully updated
        """
        data = request.json

        mother_serv.update_partial(data, fid)
        return "", 204

    def delete(self, fid):
        """
        :param fid: mother's id
        :return: code 204, if the new record in the database was successfully delete
        """
        return mother_serv.delete(fid), 204