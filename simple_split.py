# Simple string split

# Base string:
# [0] name, [1] gender, [2] age, [3] email
base_str='user,male,50,user@mail.py'

name, gender, age, email = [
    s.strip() for s in base_str.split(',')
]

print(f'User age: {age}')
