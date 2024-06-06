import random
import string


def genarateNumber(length: int):
    numbers = "".join(str(random.randint(0, 9)) for _ in range(length))
    return numbers
