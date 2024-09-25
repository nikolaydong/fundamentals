cycle_count = int(input())

positive_numbers_list = []
negative_numbers_list = []
count_positives = 0
sum_negative_numbers = 0

for _ in range(cycle_count):
    number = int(input())

    if number >= 0:
        positive_numbers_list.append(number)
        count_positives += 1
    else:
        negative_numbers_list.append(number)
        sum_negative_numbers -= number

print(positive_numbers_list)
print(negative_numbers_list)
print('Count of positives:', count_positives)
print(f'Sum of negatives: {-sum_negative_numbers}')