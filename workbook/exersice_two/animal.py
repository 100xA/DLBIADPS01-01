from abc import abstractmethod, ABC


class Animal(ABC):
    
    def __init__(self, name: str, age: int, weight: float, microchipID: int):
        self.name = name
        self.age = age
        self.weight = weight
        self.microchipID = microchipID
    
    @abstractmethod
    def noise(self):
        pass





