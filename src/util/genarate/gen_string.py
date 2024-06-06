import random
import string


def generatePassword(length: int):
    characters = string.ascii_letters + string.digits
    password = "".join(random.choice(characters) for i in range(length))
    return password
