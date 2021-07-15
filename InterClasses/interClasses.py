

class Character():
    name = ''
    race = ''
    gender = ''
    money = 0
    items = []
    equipment = {'Head': '', 'Body': '', 'Legs': ''}


class Player(Character):
    keyItems = []
    skills = []


class NPC(Character):
    chatText = []
    quests = []
