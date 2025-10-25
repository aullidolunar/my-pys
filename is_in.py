# Task: Grant access using a secret word
# Tarea: Da acceso con base en una palabra secreta

MAGIC_WORDS = {'foo', 'toor'}

user_input = input('Enter magic word: ').strip().lower()

if user_input in MAGIC_WORDS:
    print('Access granted, welcome!')
else:
    print('Access denied, bye')
