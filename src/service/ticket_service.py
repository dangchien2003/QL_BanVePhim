from src.model.ticket import Ticket
from src.util.response import Res
from src.util.valid import emailValid
from src.util.genarate import gen_number, gen_time


class TicketService:
    def __init__(self) -> None:
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

        if ticket.pricePopcorn <= 0:
            return Res(False, "Lỗi tính giá bỏng")

        if ticket.priceWater <= 0:
            return Res(False, "Lỗi tính giá nước")

        id = f"TICKET_{int(gen_time.getNowTimestamp())}_{gen_number.genarateNumber(3)}"

        ticket.setId(id)
        ticket.setAuthen("OK")
        return Res(True, data=ticket)
