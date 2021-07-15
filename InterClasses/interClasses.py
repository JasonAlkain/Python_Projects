
# base class for characters
class Character():
    name = ''
    race = ''
    gender = ''
    money = 0
    items = []
    equipment = {'Head': '', 'Body': '', 'Legs': ''}

# player class with keyitems and an array of skills
class Player(Character):
    keyItems = []
    skills = []

# NPC class for quest giver
class NPC(Character):
    chatText = []
    quests = []
