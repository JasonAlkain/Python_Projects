

# parent class
class Organism:
    name = 'Unknown'
    species = 'Unknown'
    legs = None
    arms = None
    dna = 'Sequence A'
    origin = 'Unknown'
    carbon_based = True

    def information(self):
        msg = '\n'
        msg += 'Name: {}\n'.format(self.name)
        msg += 'Species: {}\n'.format(self.species)
        msg += 'Legs: {}\n'.format(self.legs)
        msg += 'Arms: {}\n'.format(self.arms)
        msg += 'Dna: {}\n'.format(self.legs)
        msg += 'Origin: {}\n'.format(self.origin)
        msg += 'Carbon Based: {}\n'.format(self.carbon_based)
        return msg


# Child class
class Human(Organism):
    name = 'MacGuyver'
    species = 'Human'
    legs = 2
    arms = 2
    origin = 'Earth'

    def ingenuity(self):
        from hashlib import sha256
        msg = 'I am smart'.encode('utf-8')
        return sha256(msg).hexdigest()


# Child class
class Dog(Organism):
    name = 'Spot'
    species = 'Canine'
    legs = 4
    arms = 0
    dna = 'Sequence '
    origin = 'Earth'

    def speak(self):
        return 'BARK'


# Child class
class Bacterium(Organism):
    name = 'X'
    species = 'Bacterium'
    legs = 0
    arms = 0
    dna = 'Sequence C'
    origin = 'Mars'
    carbon_based = False

    def replicate(self):
        b = Bacterium
        b.name += ' (Copy)'
        return b.information(b)


if __name__ == "__main__":
    h = Human()

    print(h.information())
    print(h.ingenuity())

    d = Dog()

    print(d.information())
    print(d.speak())

    b = Bacterium()

    print(b.information())
    print(b.replicate())
