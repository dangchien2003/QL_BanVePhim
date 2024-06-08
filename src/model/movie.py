class Movie:
    def __init__(self, name, age, minPrice, time, hideAt):
        self.id = id
        self.name = name
        self.age = age
        self.minPrice = minPrice
        self.time = time
        self.hideAt = hideAt

    def __init__(self, name, age, minPrice, time):
        self.id = id
        self.name = name
        self.age = age
        self.minPrice = minPrice
        self.time = time

    def setId(self, id):
        self.id = id

    def setCreateAt(self, createAt):
        self.createAt = createAt
