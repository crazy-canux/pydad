import random
from typing import Type


class Pet:
    def __init__(self, name: str) -> None:
        self.name = name
        
    def speak(self) -> str:
        raise NotImplementedError
    
    def __str__(self) -> str:
        raise NotImplementedError

    
class Dog(Pet):
    def speak(self) -> None:
        print("woof")

    def __str__(self) -> str:
        return f"Dog<{self.name}>"


class Cat(Pet):
    def speak(self) -> None:
        print("meow")
        
    def __str__(self) -> str:
        return f"Cat<{self.name}>"


class PetShop:
    def __init__(self, animal_factory: Type[Pet]) -> None:
        self.pet_factory = animal_factory
        
    def buy_pet(self, name: str) -> Pet:
        pet = self.pet_factory(name)
        print(f"here is your {pet}")
        return pet


def random_animal(name: str) -> Pet:
    return random.choice([Dog, Cat])(name)

    
if __name__ == "__main__":
    cat_shop = PetShop(Cat)
    pet = cat_shop.buy_pet("cathy")
    pet.speak()
    
    shop = PetShop(random_animal)
    for name in ["Vis", "Min", "Next"]:
        pet = shop.buy_pet(name)
        pet.speak()
        print("-----------split-------------")