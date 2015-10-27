def getSuccessDict(message, **data):
    d = dict()
    d["message"] = message
    d["data"] = dict(**data)
    return d