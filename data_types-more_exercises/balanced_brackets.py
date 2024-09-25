lines = int(input())
previous_bracelet = ''
check_balance = 'BALANCED'

for i in range(lines):
    check_message = input()

    if check_message == '(':
        if previous_bracelet == '(':
            check_balance = 'UNBALANCED'
            break
        previous_bracelet = '('
    elif check_message == ')':
        if previous_bracelet != '(':
            check_balance = 'UNBALANCED'
            break
        previous_bracelet = ''
    else:
        continue

if previous_bracelet == '(':
    check_balance = 'UNBALANCED'

print(check_balance)
