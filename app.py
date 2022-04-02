from flask import Flask
from flask_restful import Api
from model.movie import MovieModel
from model.serie import SeriesModel
from resources.movies import Movie
from resources.series import Series, SeriesModel
from services.database import MyDatabase

app = Flask(__name__)
api = Api(app)
movie_db = MyDatabase()
series_db = MyDatabase()
MovieModel.database_service = movie_db
SeriesModel.database_service = series_db

api.add_resource(Movie, "/movie/<int:id>" , "/movie", "/movie/title/<string:title>", "/movie/genre/<string:genre>", "/movie/search/<string:search>")
#api.add_resource(Comment, "/post/<int:post_id>/comment/<int:comment_id>", "/post/<int:post_id>/comment")
api.add_resource(Series, "/series/<int:id>", "/series")

if __name__ == '__main__':
    app.run(debug=True)
