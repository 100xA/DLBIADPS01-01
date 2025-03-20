from abc import abstractmethod


class Animal:
    
    def __init__(self, name: str, alter: int, gewicht: float, microchipID: int):
        self.name = name
        self.alter = alter
        self.gewicht = gewicht
        self.microchipID = microchipID
    
    @abstractmethod
    def noise(self):
        pass





