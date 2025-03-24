from animal import Animal

class Bird(Animal):  
    def __init__(self, name: str, age: int, weight: float, microchipID: int, wingspan: float):
        super().__init__(name, age, weight, microchipID)
        self.wingspan = wingspan

    def fly(self):
        print(f"{self.name} fliegt.")

    def chirp(self):
        print(f"{self.name} Chirp!")

    def noise(self):       
        self.chirp()


            