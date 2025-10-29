from datetime import datetime

# For Python 3.10+

def workout(num):
    match num:
        case 1:
            return 'Pecho'
        case 3:
            return 'Pierna'
        case 5:
            return 'Espalda'
        case _:
            return 'No gym'

num_name=datetime.now().strftime('%A')
num_day=datetime.now().weekday()-1

print(f'{num_name}: {workout(num_day)}')
