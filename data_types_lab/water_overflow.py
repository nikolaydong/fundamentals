receive_lines = int(input())
tank_capacity = 255

for liters in range(receive_lines):
    liters_for_adding = int(input())
    if liters_for_adding > tank_capacity:
        print("Insufficient capacity!")
        continue
    tank_capacity -= liters_for_adding

print(255 - tank_capacity)