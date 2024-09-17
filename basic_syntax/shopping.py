budget = int(input())
total_price = 0

while True:
    command = input()
    if command == 'End':
        print(f'You bought everything needed.')
        break

    price_for_shopping = int(command)

    if total_price + price_for_shopping > budget:
        print(f'You went in overdraft!')
        break
    total_price += price_for_shopping