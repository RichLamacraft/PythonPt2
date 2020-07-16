import sys


while True:
    UsrInput=input('Type \'exit\' to exit: ')

    if UsrInput == 'exit':
        sys.exit()
    else:
        print('you typed:', UsrInput)
