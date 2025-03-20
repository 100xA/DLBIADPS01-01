from animal import Animal

class Cat(Animal):
    
    def __init__(self, name: str, alter: int, gewicht: float, mikrochip_id: str, favourite_toy: str):
        super().__init__(name, alter, gewicht, mikrochip_id)
        self.favourite_toy = favourite_toy
        
    def meow(self):
        print(f"{self.name} Meow!")     

    def climb(self):
        print(f"{self.name} klettert.")

    def noise(self):
        self.meow()