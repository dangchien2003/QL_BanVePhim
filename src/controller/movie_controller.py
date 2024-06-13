import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
)

from src.model.movie import Movie
from src.service.movie_service import MovieService
from src.util.response import Res


class MovieController:
    def __init__(self):
        self.movieService = MovieService()

    def checkInfoMovie(self, movie: Movie) -> Res:
        return self.movieService.checkMovie(movie)

    def convertDataTable(self, list: list[Movie]) -> Res:
        return self.movieService.convertListMovieToDataTable(list)

    def allAllMovie(self, listMovie: list[Movie]) -> Res:
        return self.movieService.addListMovie(listMovie)

    def allMovieOk(self) -> Res:
        return self.movieService.getAllMovieOk()

    def allMovie(self) -> Res:
        return self.movieService.getAllMovie()

    def allMovieHided(self) -> Res:
        return self.movieService.getAllMovieHided()

    def findMovie(self, id, name) -> Res:
        return self.movieService.findMovie(id, name)

    def getOneMovieById(self, id) -> Res:
        return self.movieService.getOneMovieById(id)

    def setHideMovie(self, id) -> Res:
        return self.movieService.hideMovie(id)

    def updateMovie(self, movie: Movie) -> Res:
        return self.movieService.updateOneMovie(movie)

    def getAllMovieInDate(self, date, format) -> Res:
        return self.movieService.getAllMovieInDate(date, format)
