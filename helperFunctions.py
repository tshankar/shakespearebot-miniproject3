def isIntegerString(s):
    try:
        i = int(s)
    except ValueError:
        return False
    return True

def flattenList(lst):
    string = ""
    for line in lst:
        string += line
    return string
