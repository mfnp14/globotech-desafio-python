import time
from json import dumps, loads
from services.database import MyDatabase

class SeriesModel: 
    database_service: MyDatabase = None

def __init__(self, title, sinopsis, genre, rating, seasons, id=None) -> None:
    if id:
        self.id = id
    else:
        highest_id = int(max(self.seek_existing_ids())) if self.seek_existing_ids() else 0
        self.id = highest_id + 1
    self.title = title
    self.sinopsis = sinopsis
    self.genre = genre
    self.rating = rating
    self.seasons = seasons

    @classmethod
    def add_series(cls, series):
        cls.database_service.create_serie(series)

    @classmethod
    def find_series(cls, series_id):
        found_series = None
        result = cls.database_service.find_series(series_id)
        print(result)
        if result:
            found_series = SeriesModel(result[1], result[2], result[3], result[4], result[5], result[0])
        return found_series

    @classmethod
    def remove_series(cls, series):
        cls.database_service.delete_series(series)

    @classmethod
    def update_movie(cls, movie):
        cls.database_service.edit_movie(movie)

    @classmethod
    def list_to_dict(cls):
        result = cls.database_service.list_series()
        series_list = []
        for series in result:
            series_list.append(SeriesModel(series[1], series[2], series[3], series[4], series[5], series[0]))
        return loads(dumps(series_list, default=SeriesModel.to_dict))

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "sinopsis": self.sinopsis,
            "genre": self.genre,
            "rating": self.rating,
            "seasons": self.seasons
        }

    @classmethod
    def seek_existing_ids(cls):
        result = cls.database_service.list_series()
        id_list = []
        for series in result:
            id_list.append(series[0])
        return sorted(id_list)