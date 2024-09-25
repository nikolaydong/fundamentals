import random

my_choice = ''
computer_choice = random.choice(['rock', 'paper', 'scissors'])

player_move = input('Choose [r] for "rock", [p] for "paper", and [s] for "scissors": ')

if player_move == 'r':
    my_choice = 'rock'
elif player_move == 'p':
    my_choice = 'paper'
elif player_move == 's':
    my_choice = 'scissors'
else:
    print('Invalid input. Try again...')

if (my_choice == 'rock' and computer_choice == 'scissors' or
        my_choice == 'paper' and computer_choice == 'rock' or
        my_choice == 'scissors' and computer_choice == 'paper'):
    print('The computer chose:', computer_choice)
    print('You Win!')
elif (my_choice == 'rock' and computer_choice == 'paper' or
      my_choice == 'paper' and computer_choice == 'scissors' or
      my_choice == 'scissors' and computer_choice == 'rock'):
    print('The computer chose:', computer_choice)
    print('You lose!')
else:
    print('The computer chose:', computer_choice)
    print('Draw!')
