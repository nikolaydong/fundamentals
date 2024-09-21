maximum_range = int(input())

for i in range(maximum_range):
    for j in range(maximum_range):
        for k in range(maximum_range):
            print(f'{chr(97 + i)}{chr(97 + j)}{chr(97 + k)}')
