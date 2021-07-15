#
#
#
# TODO: Remove the 'pass' in some of the fuctions

def start(nice=0, mean=0, name=''):
    # get user's name
    name = descsribe_game(name)
    nice, mean, name = nice_mean(nice, mean, name)


def descsribe_game(name):
    """ Check for new game """
    # If name is available then use it
    # else get the player name.
    if name != "":
        print('\nThank you for playing again, {}!'.format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input('\n\n\tWhat is your name?\n\t>>> ').capitalize()
                name = name[:12]
                if name != "":
                    print('\n')
                    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                    print('\t  Welcome, {}!'.format(name))
                    print('| In this gam , you will be greated    |')
                    print('| by several different people.         |')
                    print('| You can choose to be nice or mean    |')
                    print('| but at the end of the game your fate |')
                    print('| will be sealed by your actions.      |\n')
                    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                    stop = False
    return name


def nice_mean(nice, mean, name):
    stop = True
    prompt = '\n'
    while stop:
        show_score(nice, mean, name)
        prompt += 'A stranger approaches you \n'
        prompt += 'for a conversation. \n'
        prompt += 'Will you be: \n'
        prompt += '[N]ice or [M]ean? \n'
        prompt += '>>> '

        pick = input(prompt).lower()

        if pick == 'n':
            print('\nThe stranger walk away smilling...')
            nice = (nice + 1)
            stop = False
        if pick == 'm':
            print('\nThe stranger glares at you')
            print('menacingly and storms off...')
            mean = (mean + 1)
            stop = False

        score(nice, mean, name)


def show_score(nice, mean, name):
    print('\n{}, your current score is:'.format(name))
    print('  [ Nice: {} ] [ Mean: {} ]'.format(nice, mean))


def score(nice, mean, name):
    if nice > 2:
        win(nice, mean, name)
        pass
    if mean > 2:
        lose(nice, mean, name)
        pass
    else:
        nice_mean(nice, mean, name)
        pass


def win(nice, mean, name):
    stringVar = '\n\t~~~~~ WIN ~~~~~\n'
    stringVar += ('Nice job{}, you win!\n'.format(name))
    stringVar += ('Everyone loves you and you\'ve \n')
    stringVar += ('made lots of friends along the way!')
    print(stringVar)
    again(nice, mean, name)
    pass


def lose(nice, mean, name):
    stringVar = '\n\t~~~~~ LOSE ~~~~~\n'
    stringVar += 'Ahhh too bad {}, you lost!\n'.format(name)
    stringVar += 'You live in a dirty beat-up \n'
    stringVar += 'van down by the river, wretched \n'
    stringVar += 'and all alone \n'
    print(stringVar)
    again(nice, mean, name)
    pass


def again(nice, mean, name):
    stop = True
    while stop:
        choice = input('Do you want to play again? (y/n) \n>>> ').lower()
        if choice == "y":
            stop = False
            reset(nice, mean, name)
        if choice == "n":
            print('\nOh, so sad to see you go!')
            stop = False
            quit()
        else:
            print('\nPlease enter [Y]es or [N]o.\n')
    pass


def reset(nice, mean, name):
    nice = 0
    mean = 0
    start(nice, mean, name)


if __name__ == "__main__":
    start()
