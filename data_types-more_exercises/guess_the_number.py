import random
computer_choice = random.randint(1, 100)

print(computer_choice)
member_input = input()
member_choice = None

while member_choice != computer_choice:
    if not member_input.isdigit():
        print('Invalid input! Try again.')
        continue
    member_choice = int(member_input)
    if member_choice > computer_choice:
        print("Too high! Try again.")
    elif member_choice < computer_choice:
        print("Too low! Try again.")
    member_choice = int(input())
else:
    print(f'You guess the number!')
    print(member_choice)