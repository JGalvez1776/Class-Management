
class Student:
    def __init__(self, name, netid, gender):
        self.name = name
        self.id = netid
        self.gender = gender

    def __str__(self):
        # TODO: Make this output some html so it fits in a row
        return self.name



