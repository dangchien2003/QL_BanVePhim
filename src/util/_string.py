import string


def getPositionChar(char):
    character = char.lower()
    if character not in string.ascii_lowercase:
        return None

    position = ord(character) - ord("a") + 1
    return position
