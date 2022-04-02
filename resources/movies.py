from flask_restful import Resource, reqparse
from model.movie import MovieModel
from flask import Flask, request

class Movie(Resource):
    def get(self, id=None, title=None, search=None, genre=None):
        if id:
            found_movie = MovieModel.find_movie(id)
            if found_movie:
                return found_movie.to_dict()
            return {"message": "Movie not found"}, 404
        if title:
            found_movies = MovieModel.find_movie_by_params('title', title)
            if found_movies:
                return MovieModel.list_to_dict('title', title)
            return {"message": "Movie not found"}, 404
        if search:
            found_movies = MovieModel.find_movie_by_params('title', search)
            found_movies += MovieModel.find_movie_by_params('sinopsis', search) 
            if found_movies:
                return MovieModel.list_to_dict('search', search)
            return {"message": "Movie not found"}, 404
        if genre:
            found_movies = MovieModel.find_movie_by_params('genre', genre)
            if found_movies:
                return MovieModel.list_to_dict('genre', genre)
            return {"message": "Movie not found"}, 404
        else:
            return MovieModel.list_to_dict()


    def post(self):
        body_arguments = reqparse.RequestParser()
        body_arguments.add_argument("title")
        body_arguments.add_argument("sinopsis")
        body_arguments.add_argument("genre")
        body_arguments.add_argument("rating")
        body_arguments.add_argument("year")

        params = body_arguments.parse_args()
        #print(params.cast)
        new_movie = MovieModel(params["title"], params["sinopsis"], params["genre"], params["rating"], params["year"])
        MovieModel.add_movie(new_movie)
        return new_movie.to_dict()

    def delete(self, id):
        found_movie = MovieModel.find_movie(id)
        if found_movie:
            MovieModel.remove_movie(found_movie)
            return found_movie.to_dict()
        return {"message": "Movie not found"}, 404

    def put(self, id):
        found_movie = MovieModel.find_movie(id)
        if found_movie:
            body_arguments = reqparse.RequestParser()
            body_arguments.add_argument("title")
            body_arguments.add_argument("sinopsis")
            body_arguments.add_argument("genre")
            body_arguments.add_argument("rating")
            body_arguments.add_argument("year")
            params = body_arguments.parse_args()
            found_movie.title = params.title
            found_movie.sinopsis = params.sinopsis
            found_movie.genre = params.genre
            found_movie.rating = params.rating
            found_movie.year = params.year
            MovieModel.update_movie(found_movie)
            return found_movie.to_dict()
        return {"message": "Movie not found"}, 404   


class MovieTitle(Resource):
    """def get(self, title=None):
        if title:
            found_movie = MovieModel.find_movie_by_params(title)
            if found_movie:
                return found_movie.to_dict()
            return {"message": "Movie not found"}, 404
        else:
            return MovieModel.list_to_dict()"""

    def get(self):
        id = request.args.get('id')
        title = request.args.get('title')
        year = request.args.get('year')
        genre = request.args.get('genre')

        if id:
            list_response_movies = MovieModel.find_movie_by_params(id)
        if title:
            newMovie = MovieModel.find_movie_by_params(title)
            list_response_movies.append(newMovie)
        if year:
            newMovie = MovieModel.find_movie_by_params(year)
            list_response_movies.append(newMovie)
        if genre:
            newMovie = MovieModel.find_movie_by_params(genre)
            list_response_movies.append(newMovie)

        return list_response_movies

