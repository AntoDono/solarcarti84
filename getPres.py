from batttype import batteries

def getPres(battType):  # accepts argument of index of battery starting from 0
    return batteries.get(battType)

def description():
    return "EXCLUDED"