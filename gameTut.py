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
        prompt += '>>>: '

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


def show_score(nice, mean, name): pass


def score(nice, mean, name): pass


if __name__ == "__main__":
    start()
