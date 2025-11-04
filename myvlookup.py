# One way to emulate Excel's vlookup

mytable=[
  (0.0, 'Failed'),
  (5.0, 'Bad'),
  (7.0, 'Regular'),
  (8.0, 'Safe'),
  (9.0, 'Good'),
  (10, 'Excelent')
]

def myvlookup(value, dictable):
    last_label='unknown'
    for param, desc in dictable:
        if value < param:
            break
        last_label=desc
    return last_label

x=float(input(f'Input grade: ').strip())
ret=myvlookup(x, mytable)
print(f'{ret}')