def minLength(string, min, trim = False):
    if(trim is True):
        string = string.strip()
    
    if(len(string) < min):
        return False
    
    return True