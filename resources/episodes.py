from flask_restful import Resource, reqparse
from model.episode import EpisodeModel

class Episode(Resource):
    def get(self, id=None):
        if id:
            found_episode = EpisodeModel.find_movie(id)
            if found_episode:
                return found_episode.to_dict()
            return {"message": "Episode not found"}, 404
        else:
            return EpisodeModel.list_to_dict()
    

    def post(self):
        body_arguments = reqparse.RequestParser()
        body_arguments.add_argument("title")
        body_arguments.add_argument("sinopsis")
        body_arguments.add_argument("season")

        params = body_arguments.parse_args()
        
        new_episode = EpisodeModel(params["title"], params["sinopsis"], params["season"])
        EpisodeModel.add_movie(new_episode)
        return new_episode.to_dict()

    def delete(self, id):
        found_episode = EpisodeModel.find_movie(id)
        if found_episode:
            EpisodeModel.remove_episode(found_episode)
            return found_episode.to_dict()
        return {"message": "Episode not found"}, 404

    def put(self, id):
        found_episode = EpisodeModel.find_episode(id)
        if found_episode:
            body_arguments = reqparse.RequestParser()
            params = body_arguments.parse_args()
            found_episode.image = params.image
            return found_episode.to_dict()
        return {"message": "Episode not found"}, 404
