
choose = input('Choose a data type to perform operations on:\n'
               '1. String\n'
               '2. Numbers\n'
               '3. Booleans\n'
               '4. Additional Data Types (List, Tuple, Dictionary)\n')

if choose == '1':
    choose_string = input('You choose string\nGive me your text: ')
    if 'Python' in choose_string:
        print('PYTHON.')
        choose_string = choose_string.replace('fun!', 'awesome!')
        print(choose_string.upper())

elif choose == '2':
    number1_by_user = int(input('Now you need to give me two numbers\nPlease, give me your first number: '))
    number2_by_user = int(input('Please, give me your second number: '))
    operator = input('Now you need to choose a operator:\n'
                     'addition (+), subtraction (-), multiplication (*), and division (/): ')

    if '+' not in operator or '-' not in operator or '*' not in operator or '/' not in operator:
        print('Your choice is wrong!\nProgram exit!')

    else:
        if operator == '+':
            print(number1_by_user + number2_by_user)
        elif operator == '-':
            print(number1_by_user - number2_by_user)
        elif operator == '*':
            print(number1_by_user * number2_by_user)

        elif operator == '/':
            if number2_by_user == 0:
                print('Error! Division by zero.')
            else:
                print(number1_by_user / number2_by_user)

elif choose == '3':
    declare_python_fun = input('Is python fun? Choose between:\n1. True\n2. False\n')

    if declare_python_fun == '1':
        is_python_fun = True
    elif declare_python_fun == '2':
        is_python_fun = False

    else:
        print('Your choice is wrong!\nDefault option is set to True!')
        declare_python_fun = True
    declare_is_sun = input('Is sunny day? Choose between:\n1. True\n2. False\n')

    if declare_is_sun == '1':
        is_sunny = True
    elif declare_is_sun == '2':
        is_sunny = False
    else:
        print('Your choice is wrong!\nDefault option is set to True!')
        declare_is_sun = True
    print('Python is fun?:', is_python_fun)
    print('Is sunny day?', is_sunny)

elif choose == '4':
    specific_choice = input('You choose additional data types.\nPlease, choose between:\n1. List\n2. Tuple\n3. '
                            'Dictionary\n')
    if specific_choice == '1':
        appends = 4
        lst = []
        while appends > 0:
            for_additional = input(f'You have {appends} spaces for your list:\n')
            appends -= 1
            lst.append(for_additional)
            if appends != 0:
                print('You added a:', for_additional)
                print()
        print(lst)
        print('Your list is finished!')