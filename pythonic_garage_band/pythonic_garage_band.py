class Band:
    def __init__(self, name='The Band', members=None):
        self.name = name
        self.members = members

    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        return f"Band instance. name={self.name}, members={self.members}"


class Musician(Band):
    pass

class Guitarist(Band):
    pass

class Bassist(Band):
    pass

class Drummer(Band):
    pass
