class Ticket:
    def __init__(
        self,
        name,
        email,
        calendar,
        numPerson,
        numPopcorn,
        numWater,
        priceTicket,
        pricePopcorn,
        priceWater,
    ):
        self.name = name
        self.email = email
        self.calendar = calendar
        self.numPerson = numPerson
        self.numPopcorn = numPopcorn
        self.numWater = numWater
        self.priceTicket = priceTicket
        self.priceWater = priceWater
        self.pricePopcorn = pricePopcorn
        self.createAt = None
        self.id = None
        self.createBy = None
        self.authen = None

    def setCreateAt(self, createAt):
        self.createAt = createAt

    def setId(self, id):
        self.id = id

    def setCreateBy(self, createBy):
        self.createBy = createBy

    def setAuthen(self, authen):
        self.authen = authen
