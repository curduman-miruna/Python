class Animal:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Animal: {self.name}"
class Mammal(Animal):
    def __init__(self, name, fur_color):
        super().__init__(name)
        self.fur_color = fur_color

    def get_fur_color(self) -> str:
        return self.fur_color

    def __str__(self):
        return f"Mammal: {self.name}, Fur Color: {self.fur_color}"

class Bird(Animal):
    def __init__(self, name, wing_span, feather_color):
        super().__init__(name)
        self.wing_span = wing_span
        self.feather_color = feather_color

    def get_wing_span(self) -> float:
        return self.wing_span

    def get_feather_color(self) -> str:
        return self.feather_color

    def __str__(self):
        return f"Bird: {self.name}, Wing Span: {self.wing_span}, Feather Color: {self.feather_color}"

class Fish(Animal):
    def __init__(self, name, habitat, bone_type):
        super().__init__(name)
        self.habitat = habitat
        self.bone_type = bone_type

    def get_habitat(self) -> str:
        return self.habitat

    def get_bone_type(self) -> str:
        return self.bone_type

    def __str__(self):
        return f"Fish: {self.name}, Habitat: {self.habitat}, Bone Type: {self.bone_type}"

dog = Mammal("Cat", "White")
print(dog)
eagle = Bird("Eagle", 6.5, "Brown")
print(eagle)
salmon = Fish("Salmon", "Freshwater", "Cartilaginous")
print(salmon)





