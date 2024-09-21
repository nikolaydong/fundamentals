lost_count = int(input())
helmets = 0
swords = 0
shields = 0
armor = 0
total_expenses = 0

helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

for lost_day in range(1, lost_count + 1):
    if lost_day % 2 == 0:
        helmets += 1
    if lost_day % 3 == 0:
        swords += 1
    if lost_day % 2 == 0 and lost_day % 3 == 0:
        shields += 1
        if shields % 2 == 0:
            armor += 1
total_expenses = (helmets * helmet_price) + (swords * sword_price) + (shields * shield_price) + (armor * armor_price)

print(f"Gladiator expenses: {total_expenses:.2f} aureus")
