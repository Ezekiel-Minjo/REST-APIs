class Animal:
    def __init__(self,species,age):
        self.species = species
        self.age = age

    def describe(self):
        return f"{self.species}, {self.age} years old"

    @classmethod
    def older_animal(cls, animal):
        return cls(animal.species, animal.age + 5)

    @staticmethod
    def animal_info(animal):
        return f"Species: {animal.species}, Age: {animal.age}"

a1 = Animal("Lion", 3)
a2 = Animal.older_animal(a1)

print(a2.describe())
print(Animal.animal_info(a1))