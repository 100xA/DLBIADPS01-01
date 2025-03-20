
from dog import Dog
from cat import Cat
from bird import Bird

if __name__ == "__main__":
    doggo = Dog("Doggy", 3, 10.5, 1234567890, "16:00")
    catto = Cat("Catto", 2, 5.2, 9876543210, "18:00")
    birdo = Bird("Tweety", 1, 0.5, 1111111111, 1.2)

    doggo.noise()
    catto.noise()
    birdo.noise()
    doggo.walkDog()
    catto.climb()
    birdo.fly()
    