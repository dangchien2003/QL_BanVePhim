class Login:
    def __init__(self, email, password):
        self.email = email
        self.password = password
    def show(self):
        return self.email + self.password
    