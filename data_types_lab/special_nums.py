number = int(input())

is_special = False
sum_of_digits = 0

for count in range(1, number + 1):
    sum_of_digits = sum(int(digit) for digit in str(count))

    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        is_special = True
    else:
        is_special = False
    print(f'{count} -> {is_special}')