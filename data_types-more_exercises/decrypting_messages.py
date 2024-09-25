numbers_for_adding = int(input())
range_for_letters = int(input())

decrypted_letter = ''
decrypted_message = ''

for decrypted in range(1, range_for_letters + 1):
    letter = input()
    decrypted_letter = ord(letter) + numbers_for_adding
    decrypted_message += chr(decrypted_letter)
print(decrypted_message)
