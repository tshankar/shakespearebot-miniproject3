def isIntegerString(s):
    try:
        i = int(s)
    except ValueError:
        return False
    return True
