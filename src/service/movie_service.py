import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
)
from src.model.movie import Movie
from src.util.response import Res
from src.util.genarate import gen_number, gen_time
from src.util import number
from src.repository.movie_repository import MovieRepository


class MovieService:
    def __init__(self) -> None:
        self.movieRepository = MovieRepository()
        return

    def checkMovie(self, movie: Movie) -> Res:
        try:
            movie.name = movie.name.strip()
            movie.age = int(movie.age)
            movie.minPrice = int(movie.minPrice)
            movie.time = int(movie.time)

            if movie.name == "":
                return Res(False, "Tên phim không phù hợp")

            if movie.age != 1 and movie.age != 2 and movie.age != 3:
                return Res(False, "Tuổi xem không hợp lệ")

            if movie.minPrice <= 0:
                return Res(False, "Giá vé phải lớn hơn 0")

            if movie.time <= 0:
                return Res(False, "Thời gian phim quá ngắn")

            return Res(True)
        except Exception as e:
            print(e)
            return Res(False, "Có lỗi xảy ra")

    def convertListMovieToDataTable(self, list: list[Movie]) -> tuple:
        def convert_age(age):
            return (
                "2+"
                if age == 1
                else "16+" if age == 2 else "18+" if age == 3 else "Error"
            )

        result = [
            (
                movie.name,
                convert_age(movie.age),
                f"{number.convertPrice(movie.minPrice)} đ",
                f"{movie.time} phút",
            )
            for movie in list
        ]

        return Res(True, data=result)

    def addListMovie(self, list: list[Movie]) -> bool:
        try:
            if len(list) == 0:
                return Res(False, "Không có dữ liệu")

            now = gen_time.getNowTimestamp()
            for movie in list:
                id = f"MOVIE_{int(now)}_{gen_number.genarateNumber(5)}"
                movie.setId(id)
                movie.setCreateAt(now)
                movie.age = (
                    2
                    if movie.age == 1
                    else 16 if movie.age == 2 else 18 if movie.age == 3 else 0
                )

            dataInsert = [
                (
                    movie.id,
                    movie.name,
                    movie.age,
                    movie.minPrice,
                    movie.createAt,
                    movie.time,
                )
                for movie in list
            ]

            rowAffect = self.movieRepository.insertListMovie(dataInsert)

            if rowAffect == 0:
                return Res(False, "Thêm thất bại")

            return Res(True, data=rowAffect)
        except (Exception, ValueError) as e:
            print(e)
            return Res(False, "Có lỗi xảy ra")

    def getAllMovieOk(self) -> Res:
        data = self.movieRepository.GetAllMovieOk()
        if data is None:
            return Res(False, "Lỗi truy vấn")

        return Res(True, data=data)

    def getAllMovie(self) -> Res:
        data = self.movieRepository.GetAllMovie()
        if data is None:
            return Res(False, "Lỗi truy vấn")

        return Res(True, data=data)

    def getAllMovieHided(self) -> Res:
        data = self.movieRepository.GetAllMovieHided()
        if data is None:
            return Res(False, "Lỗi truy vấn")

        return Res(True, data=data)

    def findMovie(self, id, name) -> Res:
        if id.strip() == "" and name.strip() == "":
            return Res(False, "Nhập thông tin phim")

        data = None

        if id.strip() != "" and name.strip() != "":
            data = self.movieRepository.findMovieByIdAndName(id, name)
        elif id.strip() != "":
            data = self.movieRepository.findMovieById(id)
        else:
            data = self.movieRepository.findMovieByName(name)

        if data is None:
            return Res(False, "Lỗi truy vấn dữ liệu")

        return Res(True, data=data)

    def getOneMovieById(self, id) -> Res:
        if id.strip() == "":
            return Res(False, "Id không tồn tại")

        data = self.movieRepository.findMovieById(id)

        if data is None:
            return Res(False, "Lỗi truy vấn dữ liệu")

        if len(data) == 0:
            return Res(False, "Không tìm thấy dữ liệu")

        return Res(True, data=data[0])

    def hideMovie(self, id):
        if id.strip() == "":
            return Res(False, "Id không tồn tại")

        now = gen_time.getNowTimestamp()

        rowAffect = self.movieRepository.hideMovie(id, now)
        if rowAffect is None:
            return Res(False, "Lỗi truy vấn dữ liệu")

        elif rowAffect == 0:
            return Res(False, "Không thể dừng chiếu")

        return Res(True, data=now)

    def updateOneMovie(self, movie: Movie) -> Res:
        if movie.id.strip() == "":
            return Res(False, "Id không hợp lệ")

        # convert age
        movie.age = (
            2
            if movie.age == 1
            else 16 if movie.age == 2 else 18 if movie.age == 3 else 0
        )

        rowAffect = self.movieRepository.updateOneMovie(movie)

        if rowAffect is None:
            return Res(False, "Lỗi truy vấn dữ liệu")

        if rowAffect == 0:
            return Res(False, "Id Không tồn tại hoặc không có bất kỳ thay đổi nào")

        return Res(True)
