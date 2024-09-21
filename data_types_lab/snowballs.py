numb_snowballs = int(input())
max_snowball_weight = 0
max_snowball_time = 0
max_snowball_quality = 0
max_result = 0

for current_ball in range(numb_snowballs):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    current_result = (snowball_weight / snowball_time) ** snowball_quality
    if current_result > max_result:
        max_snowball_weight = snowball_weight
        max_snowball_time = snowball_time
        max_snowball_quality = snowball_quality
        max_result = int(current_result)
    result = f'{max_snowball_weight} : {max_snowball_time} = {max_result} ({max_snowball_quality})'

print(result)