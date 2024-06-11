class Movie:

    def __init__(self, name, age, minPrice, time):
        self.name = name
        self.age = age
        self.minPrice = minPrice
        self.time = time
        self.hideAt = None

    def setId(self, id):
        self.id = id

    def setCreateAt(self, createAt):
        self.createAt = createAt

    def setHideAt(self, hideAt):
        self.hideAt = hideAt
