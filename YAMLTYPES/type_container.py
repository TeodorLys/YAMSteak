
#Global GUI Items

objs: list = []

class container:
    def __init__(self):
        pass

    def handle(self):
        for o in objs:
            o.begin()