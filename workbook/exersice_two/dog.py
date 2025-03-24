from animal import Animal

class Dog(Animal):
    def __init__(self, name: str, age: int, weight: float, microchipID: int, walking_time: str):
        super().__init__(name, age, weight, microchipID)
        self.walking_time = walking_time

    def woof(self):
        print(f"{self.name} Woof!")

    def walkDog(self):
        print(f"{self.name} geht um {self.walking_time} Uhr Gassi.")

    def noise(self):
        self.woof()

