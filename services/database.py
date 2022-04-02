import sqlite3

class MyDatabase:
    def __init__(self) -> None:
        self._db_connection = sqlite3.connect("movie_archive.db", check_same_thread=False)
        self._cursor = self._db_connection.cursor()
        create_movie_table = "CREATE TABLE IF NOT EXISTS movie (movie_id integer PRIMARY KEY, title text, \
            sinopsis text, genre text, rating INTEGER, year INTEGER)"
        self._cursor.execute(create_movie_table)
        self._db_connection.commit()

    def create_movie(self, movie):
        create_movie_SQL = "INSERT INTO movie VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(movie.id, movie.title, movie.sinopsis, movie.genre, movie.rating, movie.year)
        self._cursor.execute(create_movie_SQL)
        self._db_connection.commit()

    def list_movies(self):
        list_movies_SQL = "SELECT * from movie;"
        return self._cursor.execute(list_movies_SQL).fetchall()

    def delete_movie(self, movie):
        delete_movie_SQL = "DELETE FROM movie WHERE movie_id='{}'".format(movie.id)
        self._cursor.execute(delete_movie_SQL)
        self._db_connection.commit()

    def find_movie(self, movie_id):
        select_movie_SQL = "SELECT * FROM movie WHERE movie_id='{}'".format(movie_id)
        return self._cursor.execute(select_movie_SQL).fetchone()
    
    def search_filter(self, search_field, search_key):
        print(search_key)
        select_movie_by_title_SQL = "SELECT * FROM movie WHERE {} LIKE '%{}%'".format(search_field, search_key)
        return self._cursor.execute(select_movie_by_title_SQL).fetchall()

        # self.cursor.execute(
        #     "select string from stringtable where string like ? and type = ?",
        #     ('%'+searchstr+'%', type))

    def edit_movie(self, movie):
        edit_movie_SQL = """UPDATE movie SET title = '{}', sinopsis = '{}', genre = '{}', rating = '{}', year = '{}' WHERE movie_id='{}'""".format(movie.title, movie.sinopsis, movie.genre, movie.rating,
                                                        movie.year, movie.id)
        self._cursor.execute(edit_movie_SQL)
        self._db_connection.commit()

    def __del__(self):
        self._db_connection.close()