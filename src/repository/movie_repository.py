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
