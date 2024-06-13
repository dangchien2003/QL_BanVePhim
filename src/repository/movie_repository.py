import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
)

from src.util.excute import Excute
from src.model.movie import Movie


class MovieRepository:
    def __init__(self):
        self.excute = Excute()

    def insertListMovie(self, list: list[Movie]) -> int:
        query = "INSERT INTO movie(id, name, age, minPrice, createAt, time) VALUES(%s, %s, %s, %s, %s, %s)"
        return self.excute.editMany(query, list)

    def GetAllMovieOk(self) -> tuple:
        query = "SELECT id, name, age, minPrice, time, hideAt, createAt FROM movie where hideAt is null order by createAt;"
        return self.excute.getAll(query)

    def GetAllMovie(self) -> tuple:
        query = "SELECT id, name, age, minPrice, time, hideAt, createAt FROM movie order by createAt;"
        return self.excute.getAll(query)

    def GetAllMovieHided(self) -> tuple:
        query = "SELECT id, name, age, minPrice, time, hideAt, createAt FROM movie where hideAt is not null order by createAt;"
        return self.excute.getAll(query)

    def findMovieByIdAndName(self, id, name):
        query = f"SELECT id, name, age, minPrice, time, hideAt, createAt FROM movie where name like '%{name}%' or id = '{id}' order by createAt;"
        return self.excute.getAll(query)

    def findMovieById(self, id):
        query = f"SELECT id, name, age, minPrice, time, hideAt, createAt FROM movie where id = '{id}' order by createAt;"
        return self.excute.getAll(query)

    def findMovieByName(self, name):
        query = f"SELECT id, name, age, minPrice, time, hideAt, createAt FROM movie where name like '%{name}%' order by createAt;"
        return self.excute.getAll(query)

    def hideMovie(self, id, timestamp):
        query = f"update movie set hideAt = '{timestamp}' where id = '{id}';"
        return self.excute.edit(query)

    def updateOneMovie(self, movie: Movie):
        query = f"update movie set name = '{movie.name}', age = {movie.age}, minPrice = {movie.minPrice}, time = {movie.time} where id = '{movie.id}'"
        return self.excute.edit(query)

    def getAllMovieFromTo(self, start: float, end: float):
        query = f"""SELECT 
                        movie.id ,  
                        movie.name
                    FROM 
                        movie 
                    JOIN 
                        calendar 
                    ON 
                        movie.id = calendar.idMovie 
                    WHERE 
                        calendar.cancleAt IS NULL  
                    AND
                        movie.hideAt IS NULL
                    AND 
                        calendar.time BETWEEN {start} AND {end}"""
        return self.excute.getAll(query)
