class Film(object):

    def __init__(self, title="", year=""):
        self.title = title
        self.year = year

    @classmethod
    def random(cls):
        from random import randint
        return cls(title="film" + str(randint(0, 1000000)),
                   year=randint(1895, 2020))