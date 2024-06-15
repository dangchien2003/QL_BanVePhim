from src.model.ticket import Ticket
from src.service.order_service import OrderService
from src.util.response import Res


class OrderController:
    def __init__(self):
        self.orderService = OrderService()

    def orderTicket(self, ticket: Ticket, chairs: list, idStaff: str) -> Res:
        return self.orderService.order(ticket, chairs, idStaff)
