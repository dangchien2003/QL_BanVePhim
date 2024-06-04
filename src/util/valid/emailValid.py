import re

def isEmail(email):
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Sử dụng re.match để kiểm tra email
    if re.match(regex, email):
        return True
    else:
        return False
    