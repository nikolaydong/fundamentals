text = input().lower()

counter_sand = text.count('sand')
counter_water = text.count('water')
counter_fish = text.count('fish')
counter_sun = text.count('sun')

print(counter_sand + counter_water + counter_fish + counter_sun)