from flask_restful import Resource, reqparse
from model.serie import SeriesModel

class Series(Resource):
    def get(self, id=None):
        if id:
            found_serie = SeriesModel.find_serie(id)
            if found_serie:
                return found_serie.to_dict()
            return {"message": "Series not found"}, 404
        else:
            return SeriesModel.list_to_dict()

    def post(self):
        body_arguments = reqparse.RequestParser()
        body_arguments.add_argument("title")
        body_arguments.add_argument("sinopsis")
        body_arguments.add_argument("genre")
        body_arguments.add_argument("rating")
        body_arguments.add_argument("seasons")

        params = body_arguments.parse_args()
        new_serie = SeriesModel(params["title"], params["sinopsis"], params["genre"], params["rating"], params["seasons"])
        SeriesModel.add_serie(new_serie)
        return new_serie.to_dict()

    def delete(self, id):
        found_serie = SeriesModel.find_serie(id)
        if found_serie:
            SeriesModel.remove_serie(found_serie)
            return found_serie.to_dict()
        return {"message": "Series not found"}, 404

    def put(self, id):
        found_serie = SeriesModel.find_serie(id)
        if found_serie:
            body_arguments = reqparse.RequestParser()
            params = body_arguments.parse_args()
            return found_serie.to_dict()
        return {"message": "Series not found"}, 404

    class SerieTitle(Resource):
        def get(self, title=None):
            if title:
                found_serie = SeriesModel.find_serie_by_params(title)
                if found_serie:
                    return found_serie.to_dict()
                else:
                    return {"message": "Series not found"}, 404
            else:
                return SeriesModel.list_to_dict()
