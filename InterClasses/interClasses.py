
# base class for characters
class Character():
    def __init__(self, name, race, gender):
        self.name = name
        self.race = race
        self.gender = gender

    def characterInfo(self):
        msg = '\n'
        msg += 'Name: {}'.format(self.name)
        msg += 'Race: {}'.format(self.race)
        msg += 'Gender: {}'.format(self.gender)
        return msg

# player class with keyitems and an array of skills


class Player(Character):
    def __init__(self, name, race, gender, skills, money, itmes, equipment):
        super().__init__(name, race, gender)
        self.skills = skills
        self.money = money
        self.itmes = itmes
        self.equipment = equipment

    def characterInfo(self):
        msg = '\n'
        msg += 'Name: {}\n'.format(self.name)
        msg += 'Race: {}\n'.format(self.race)
        msg += 'Gender: {}\n'.format(self.gender)
        msg += 'Skills: {}\n'.format(self.skills)
        msg += 'Money: {}\n'.format(self.money)
        msg += 'Items: {}\n'.format(self.itmes)
        if equipment != None:
            msg += 'Equipment:\n'
            for equip in self.equipment:
                msg += '\t{}: {}\n'.format(equip, self.equipment[equip])
        return msg


# NPC class for quest giver
class NPC(Character):
    chatText = []
    quests = []


if __name__ == "__main__":
    equipment = {'Head': None, 'Body': 'Shirt', 'Legs': 'Pants'}

    fname = input('What is your first name: ').capitalize()
    lname = input('What is your last name: ').capitalize()
    name = '{} {}'.format(fname, lname)

    race = input('What is your race: ').capitalize()
    gender = input('What is your gender: ').capitalize()

    player_1 = Player(name, race, gender, [], 0, [], equipment)
    print(player_1.characterInfo())
