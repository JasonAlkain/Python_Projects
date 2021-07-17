
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
        self.items = items
        self.equipment = equipment

    # return the info of this class
    def info(self):
        msg = '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
        msg += super().info()  # get the info function

        # check if there were any skills passed to the class
        if self.skills != None:
            msg += 'Skills:\n'
            for skill in self.skills:
                msg += '\t{}\n'.format(skill)

        # print the players money
        # TODO: Add a type check here
        msg += 'Money: {}\n'.format(self.money)

        # check if there were any items passed to the class
        if self.items != None:
            msg += 'Items:\n'
            for item in self.items:
                msg += '\t{}\n'.format(item)

        # check if there was any equipment passed to the class
        if self.equipment != None:
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
                msg += '\t{}\n'.format(chat)

        # check if there was any equipment passed to the class
        if self.quests != None:
            msg += 'quests:\n'
            for quest in self.quests:
                msg += '\t{}\n'.format(quest)

        msg += '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
        return msg


def newPlayer():
    # request player for first and last name
    fname = input('What is your first name: ').capitalize()
    lname = input('What is your last name: ').capitalize()
    # add first and last name together to make one name
    name = '{} {}'.format(fname, lname)
    # request player for  race
    race = input('What is your race: ').capitalize()
    # request player for gender
    gender = input('What is your gender: ').capitalize()
    # Setup basic skills
    skills = ['Magic Missile', 'Friends (Concentration)', 'Mage Hand']
    # Setup money
    money = 50
    # Setup items
    items = ['Potion of healing', 'Smart Phone']
    # create basic equipment
    equipment = {'Head': None, 'Body': 'Shirt', 'Legs': 'Pants'}
    # return the completed player object
    return Player(name, race, gender, skills, money, items, equipment)


if __name__ == "__main__":
    player_1 = newPlayer()
    print(player_1.info())

    npc = NPC('Jake', 'Human', 'Male', ["I'm Jake from State Farm."], None)
    print(npc.info())
