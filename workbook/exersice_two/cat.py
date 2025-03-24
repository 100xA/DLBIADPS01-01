from animal import Animal

class Cat(Animal):
    
    def __init__(self, name: str, age: int, weight: float, microchipID: int, favourite_toy: str):
        super().__init__(name, age, weight, microchipID)
        self.favourite_toy = favourite_toy
        
    def meow(self):
        print(f"{self.name} Meow!")     

    def climb(self):
        print(f"{self.name} klettert.")

    def noise(self):
        self.meow()