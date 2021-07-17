
# base class for characters
class Character():
    # initialize the class with basic variables
    def __init__(self, name, race, gender):
        self.name = name
        self.race = race
        self.gender = gender

    # return the info of this class
    def info(self):
        msg = '\n'
        msg = 'Name: {}\n'.format(self.name)
        msg += 'Race: {}\n'.format(self.race)
        msg += 'Gender: {}\n'.format(self.gender)
        return msg

# player class with keyitems and an array of skills


class Player(Character):
    # initialize the class
    def __init__(self, name, race, gender, skills, money, items, equipment):
        # Include the original initialization from the parent class
        super().__init__(name, race, gender)
        self.skills = skills
        self.money = money
        self.itmes = items
        self.equipment = equipment

    # return the info of this class
    def info(self):
        msg = '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
        msg += super().info()  # get the info function

        # check if there were any skills passed to the class
        if self.skills != None:
            msg += 'Skills:\n'
            for skill in self.skills:
                msg += '| {}\n'.format(skill)

        # print the players money
        # TODO: Add a type check here
        msg += 'Money: {}\n'.format(self.money)

        # check if there were any items passed to the class
        if self.itmes != None:
            msg += 'Items:\n'
            for item in self.items:
                msg += '| {}\n'.format(item)

        # check if there was any equipment passed to the class
        if equipment != None:
            msg += 'Equipment:\n'
            for equip in self.equipment:
                msg += '\t{}: {}\n'.format(equip, self.equipment[equip])
        msg += '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
        return msg


# NPC class for quest giver
class NPC(Character):
    # initialize the class
    def __init__(self, name, race, gender, chatText, quests):
        # Include the original initialization from the parent class
        super().__init__(name, race, gender)
        self.chatText = chatText
        self.quests = quests

    # return the info of this class
    def info(self):
        msg = '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
        msg += super().info()  # get the info function

        # check if there was any quests passed to the class
        if self.chatText != None:
            msg += 'Chat:\n'
            for chat in self.chatText:
                msg += '| {}\n'.format(chat)

        # check if there was any equipment passed to the class
        if self.quests != None:
            msg += 'quests:\n'
            for quest in self.quests:
                msg += '| {}\n'.format(quest)

        msg += '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
        return msg


if __name__ == "__main__":
    equipment = {'Head': None, 'Body': 'Shirt', 'Legs': 'Pants'}

    fname = input('What is your first name: ').capitalize()
    lname = input('What is your last name: ').capitalize()
    name = '{} {}'.format(fname, lname)

    race = input('What is your race: ').capitalize()
    gender = input('What is your gender: ').capitalize()

    player_1 = Player(name, race, gender, None, 0, None, equipment)
    print(player_1.info())

    npc = NPC('Jake', 'Human', 'Male', ["I'm Jake from State Farm."], None)
    print(npc.info())
