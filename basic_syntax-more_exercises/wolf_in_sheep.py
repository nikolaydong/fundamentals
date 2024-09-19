animal = input().split(', ')

wolf_index = animal.index("wolf")

if animal[-1] == 'wolf':
    print('Please go away and stop eating my sheep')
else:
    sheep_attention = len(animal) - wolf_index - 1
    print(f'Oi! Sheep number {sheep_attention}! You are about to be eaten by a wolf!')