myFile = open('Name.txt')
lists = myFile.read().split()
myFile.close()


def replay():
    # type: () -> Boolean
    """
    :return: This will return a Boolean Value for game play
    """
    option = raw_input('Do you want to try again? (y/n)\nTo view all name press "a"').upper()
    if option.startswith('Y'):
        return True

    elif option.startswith('A'):
        print lists
        replay()

    else:
        return False


start = True

while start:
    name = raw_input('Input your name: ')

    for l in lists:
        if l == name:
            print 'Name Found!!'
            break
    else:
        myFile1 = open('Name.txt', 'a')
        myFile1.write(' ' + name)
        myFile1.close()
        print 'Not Found! Name added'

    start = replay()
