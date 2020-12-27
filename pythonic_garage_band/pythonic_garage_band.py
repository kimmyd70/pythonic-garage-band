class Band:
    instances = []
    
    def __init__(self, name='The Band', members = None):
        self.name = name
        self.members = members

    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        return f"Band instance. name={self.name}, 
        members={self.members}"
        
    def play_solos(self):
        solos = []
        for player in self.members:
            solos.append(player.play_solo())
        return solos
    
    @classmethod
    def to_list(cls):
        return cls.instances


class Musician(Band):
        def __init__(self, name='Rock God', instrument=None):
        self.name = name
        self.instrument = instrument

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f"{self.__class__.__name__} instance. Name={self.name}"
    
    def get_instrument(self)
        return self.instrument
        
    # def play_solos(self):
    #     return "face melting guitar solo"


class Guitarist(Musician):
    def __str__(self):
        return f'My name is {self.name} and I play guitar'
    
    def __repr__(self):
        return f'Guitarist instance. Name = {self.name}'
    
    def get_instrument(self):
        return 'guitar'
    
    def play_solos(self):
        return "face melting guitar solo"

class Bassist(Musician):
        def __str__(self):
        return f'My name is {self.name} and I play bass'
    
    def __repr__(self):
        return f'Bassist instance. Name = {self.name}'
    
    def get_instrument(self):
        return 'bass'
    
    def play_solos(self):
        return "bom bom buh bom"


class Drummer(Musician):
    def __str__(self):
        return f'My name is {self.name} and I play drums'
    
    def __repr__(self):
        return f'Drummer instance. Name = {self.name}'
    
    def get_instrument(self):
        return 'drums'
    
    def play_solos(self):
        return "rattle boom crash"
    
if __name__ == '__main__':
    muscian = Musician('Joe', 'flute')
    print(repr(musician))
    
    guitarist = Guitarist('Jane', 'guitar')
    print guitarist
