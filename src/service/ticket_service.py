from src.model.ticket import Ticket
from src.model.checkin_ticket import InfoCheckin
from src.service.render_template_service import RenderHtml
from src.service.mail_service import MailService
from src.repository.ticket_repository import TicketRepository
from src.repository.seat_repository import SeatRepository
from src.util.response import Res
from src.util.valid import emailValid
from src.util.genarate import gen_number, gen_time
from src.util import time


class TicketService:
    def __init__(self) -> None:
        self.renderService = RenderHtml()
        self.mailService = MailService()
        self.seatRepository = SeatRepository()
        self.ticketRepository = TicketRepository()
        return

    def checkInfoTicket(self, ticket: Ticket) -> Res:
        if ticket is None:
            return Res(False, "Không có thông tin")

        if ticket.name.strip() == "":
            return Res(False, "Thiếu tên khách hàng")

        if ticket.email.strip() == "":
            return Res(False, "Thiếu email khách hàng")

        if emailValid.isEmail(ticket.email.strip()) is False:
            return Res(False, "Email không đúng")

        if ticket.calendar is None or ticket.calendar.strip() == "":
            return Res(False, "Không có mã lịch chiếu")

        if ticket.numPerson == 0:
            return Res(False, "Số ghế phải lớn hơn 0")

        if ticket.numPopcorn < 0:
            return Res(False, "Số lượng bỏng không âm")

        if ticket.numWater < 0:
            return Res(False, "Số lượng nước không âm")

        if ticket.priceTicket <= 0:
            return Res(False, "Lỗi tính giá vé")

        if ticket.pricePopcorn < 0:
            return Res(False, "Lỗi tính giá bỏng")

        if ticket.priceWater < 0:
            return Res(False, "Lỗi tính giá nước")

        id = f"TICKET_{int(gen_time.getNowTimestamp())}_{gen_number.genarateNumber(3)}"

        ticket.setId(id)
        ticket.setAuthen("OK")
        return Res(True, data=ticket)

    def sendMail(self, idticket, movie, calendar, chairs, customer, to_email) -> Res:
        if (
            idticket is None
            or movie is None
            or calendar is None
            or chairs is None
            or customer is None
            or idticket.strip() == ""
            or movie.strip() == ""
            or calendar.strip() == ""
            or customer.strip() == ""
            or len(chairs) == 0
        ):
            return Res(False, "Thiếu thông tin")

        content = {
            "movie": movie,
            "calendar": calendar,
            "chairs": ", ".join(chairs),
            "ticket": idticket,
            "customer": customer.title(),
        }
        body = self.renderService.generate_html("mail_ticket.html", content)

        email = MailService()
        result = email.SendMail("Thông tin vé phim", body, to_email)
        if result == False:
            return Res(False, "Lỗi gửi mail")
        return Res(True)

    def getInfoTicket(self, ticket):
        if ticket == None or ticket.strip() == "":
            return Res(False, "Không tìm thấy mã vé")

        resultTicket = self.ticketRepository.getInfoTicket(ticket)

        if resultTicket is None:
            return Res(False, "Lỗi truy vấn dữ liệu")

        if len(resultTicket) == 0:
            return Res(False, "Vé không tồn tại")

        resultTicket = list(resultTicket[0])
        if resultTicket[6] is not None:
            return Res(False, "Vé đã được sử dụng")
        if resultTicket[7] * 60 + resultTicket[1] < gen_time.getNowTimestamp():
            return Res(False, "Vé đã hết hạn sử dụng")

        if resultTicket[1] - gen_time.getNowTimestamp() > 15 * 60:
            return Res(
                False,
                f"Sử dụng vé quá sớm\nPhim chiếu lúc: {time.convertTimeStampToString(resultTicket[1], '%H:%M %d-%m-%Y')}",
            )

        resultSeat = self.seatRepository.getInfoSeat(ticket)
        resultSeat = [item for tup in resultSeat for item in tup]

        info: InfoCheckin = InfoCheckin(
            resultTicket[0],
            time.convertTimeStampToString(resultTicket[1], "%H:%M %d-%m-%Y"),
            resultTicket[2],
            resultTicket[3],
            ",".join(resultSeat),
            resultTicket[4],
            resultTicket[5],
        )
        return Res(True, data=info)

    def checkinTicket(self, ticket, staff) -> Res:
        if ticket == None or ticket.strip() == "":
            return Res(False, "Không tìm thấy mã vé")

        result = self.ticketRepository.checkin(
            ticket, gen_time.getNowTimestamp(), staff
        )

        if result is None:
            return Res(False, "Lỗi truy vấn dữ liệu")

        if result == 0:
            return Res(False, "Không thể checkin")

        return Res(True)
