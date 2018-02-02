
with open("input.txt") as f:
    l = f.read()[:-1].split(',')

steps = {}
steps['n'] = 0
steps['nw'] = 0
steps['ne'] = 0

for d in l:
    if d == 'n':
        steps['n'] += 1

    elif d == 's':
        steps['n'] -= 1

    elif d == 'nw':
        steps['nw'] += 1

    elif d == 'se':
        steps['nw'] -= 1

    elif d == 'ne':
        steps['ne'] += 1

    elif d == 'sw':
        steps['ne'] -= 1

while steps['nw'] > 0 and steps['ne'] > 0:
    steps['n'] += 1
    steps['nw'] -= 1
    steps['ne'] -= 1

while steps['nw'] < 0 and steps['ne'] < 0:
    steps['n'] -= 1
    steps['nw'] += 1
    steps['ne'] += 1

while steps['n'] > 0 and steps['nw'] < 0:
    steps['ne'] += 1
    steps['n'] -= 1
    steps['nw'] += 1

while steps['n'] < 0 and steps['nw'] > 0:
    steps['ne'] -= 1
    steps['n'] += 1
    steps['nw'] -= 1

while steps['n'] > 0 and steps['ne'] < 0:
    steps['nw'] += 1
    steps['n'] -= 1
    steps['ne'] += 1

while steps['n'] < 0 and steps['ne'] > 0:
    steps['nw'] -= 1
    steps['n'] += 1
    steps['ne'] -= 1
