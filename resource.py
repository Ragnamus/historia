class Resdata():
    def __init__(self, count):
        self.count = count

class Resource():
    def __init__(self, restype, count):
        self.key = restype
        self.resdata = Resdata(count)
