cycle_count = int(input())
filtered_list = []
my_list = []

for _ in range(cycle_count):
    integer = int(input())
    my_list.append(integer)

command = input()

if command == 'even':
    for index in my_list:
        if index % 2 == 0:
            filtered_list.append(index)

elif command == 'odd':
    for index in my_list:
        if index % 2 != 0 and index >= 0:
            filtered_list.append(index)

elif command == 'positive':
    for index in my_list:
        if index >= 0:
            filtered_list.append(index)

elif command == 'negative':
    for index in my_list:
        if index < 0:
            filtered_list.append(index)

print(filtered_list)