cycle_count = int(input())

special_word = input()
base_list = []
special_word_list = []

for _ in range(cycle_count):
    some_text = input()
    if special_word in some_text:
        special_word_list.append(some_text)
    base_list.append(some_text)

print(base_list)
print(special_word_list)