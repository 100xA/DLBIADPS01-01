from animal import Animal

class Dog(Animal):
    def __init__(self, name: str, alter: int, gewicht: float, mikrochip_id: str, gassi_gehen_zeit: str):
        super().__init__(name, alter, gewicht, mikrochip_id)
        self.gassi_gehen_zeit = gassi_gehen_zeit

    def woof(self):
        print(f"{self.name} Woof!")

    def walkDog(self):
        print(f"{self.name} geht um {self.gassi_gehen_zeit} Uhr Gassi.")

    def noise(self):
        self.woof()

