from animal import Animal
from abc import abstractmethod

class Bird(Animal):  
    def __init__(self, name: str, alter: int, gewicht: float, mikrochip_id: str, wingspan: float):
        super().__init__(name, alter, gewicht, mikrochip_id)
        self.wingspan = wingspan

    def fly(self):
        print(f"{self.name} fliegt.")

    def chirp(self):
        print(f"{self.name} Chirp!")

    def noise(self):       
        self.chirp()


            