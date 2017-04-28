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
        return True

    else:
        return False


start = True

while start:
    myFile = open('Name.txt')
    lists = myFile.read().split()
    myFile.close()

    name = raw_input('Input your name: ')

    for l in lists:
        if l == name:
            print 'Name Found!!'
            break
    else:
        print 'Not Found!'
        if raw_input('Do you wanna add the name?(y/n)').upper().startswith('Y'):
            myFile1 = open('Name.txt', 'a')
            myFile1.write(' ' + name)
            myFile1.close()

    start = replay()
