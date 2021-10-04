class Animals():
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def __init__(self, name, age):
        self.name = name
        self.age = age

class Zebra(Animals):
    def get_species(self):
        return self.species

    def __init__(self, name, age, species):
        super().__init__(name, age)
        self.species = species

    def __repr__(self):
        print(self.name, self.age, self.species, '\n')
        pass

class Dolphin(Animals):
    def get_species(self):
        return self.species

    def __init__(self, name, age, species):
        super().__init__(name, age)
        self.species = species

    def __repr__(self):
        print(self.name, self.age, self.species, '\n')
        pass


if __name__ == "__main__":
    a = Animals('Name', 10)
    z = Zebra('George', 9, 'Zebra')
    d = Dolphin('Lucky', 7, 'Dolphin')
    print(a.get_name(), a.get_age())
    print(z.get_name(), z.get_age(), z.get_species())
    print(d.get_name(), d.get_age(), d.get_species())