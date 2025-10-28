import random, time

mylist = ['Python', 'Perl', 'Ruby', 'PHP', 'Java']

lang = None

print(f'Ready... ', end='')
time.sleep(2) # wait 2 secs
print(f'Set... ', end='')
time.sleep(2)
print(f'Go!')
while lang != 'Python':
    lang = random.choice(mylist)
    print(f'{" " * 5}{lang}') # '     Perl'
    time.sleep(2)
print(f'Done')