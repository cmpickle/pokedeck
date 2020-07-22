class Pokecard(object):
    def __init__(self, id, name, series, set):
        self.id = id
        self.name = name
        self.series = series
        self.set = set

    def __str__(self):
        return '{self.id} {self.name} {self.series} {self.set}'.format(self=self)
