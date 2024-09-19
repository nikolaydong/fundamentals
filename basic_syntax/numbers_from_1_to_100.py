# pattern :: heart

number = int(input(''))

for column in range(number + 1):
    for rows in range(number - column):
        print(' ', end='')
    for row in range(2 * column + 1):
        print('*', end='')
    print()