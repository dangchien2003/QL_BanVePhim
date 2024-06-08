import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
)

from src.model.movie import Movie
from src.service.movie_service import MovieService


class MovieController:
    def __init__(self):
        self.movieService = MovieService()

    def checkInfoMovie(self, movie: Movie) -> bool:
        return self.movieService.checkMovie(movie)

    def convertDataTable(self, list: list[Movie]):
        return self.movieService.convertListMovieToDataTable(list)

    def allAllMovie(self, listMovie: list[Movie]):
        return self.movieService.addListMovie(listMovie)
