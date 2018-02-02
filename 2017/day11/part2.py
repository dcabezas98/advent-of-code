with open("input.txt") as f:
    l = f.read()[:-1].split(',')

steps = {}
steps['n'] = 0
steps['nw'] = 0
steps['ne'] = 0

def normalize():

    normal = True

    while steps['nw'] > 0 and steps['ne'] > 0:
        steps['n'] += 1
        steps['nw'] -= 1
        steps['ne'] -= 1
        normal = False

    while steps['nw'] < 0 and steps['ne'] < 0:
        steps['n'] -= 1
        steps['nw'] += 1
        steps['ne'] += 1
        normal = False

    while steps['n'] > 0 and steps['nw'] < 0:
        steps['ne'] += 1
        steps['n'] -= 1
        steps['nw'] += 1
        normal = False

    while steps['n'] < 0 and steps['nw'] > 0:
        steps['ne'] -= 1
        steps['n'] += 1
        steps['nw'] -= 1
        normal = False

    while steps['n'] > 0 and steps['ne'] < 0:
        steps['nw'] += 1
        steps['n'] -= 1
        steps['ne'] += 1
        normal = False

    while steps['n'] < 0 and steps['ne'] > 0:
        steps['nw'] -= 1
        steps['n'] += 1
        steps['ne'] -= 1
        normal = False

    if not normal:
        normalize()

        
def distance():
    normalize()
    return abs(steps['n']) + abs(steps['ne']) + abs(steps['nw'])

furthest = 0

for i in l:
    if i == 'n':
        steps['n'] += 1

    elif i == 's':
        steps['n'] -= 1

    elif i == 'nw':
        steps['nw'] += 1

    elif i == 'se':
        steps['nw'] -= 1

    elif i == 'ne':
        steps['ne'] += 1

    elif i == 'sw':
        steps['ne'] -= 1

    d = distance()
    
    if d > furthest:
        furthest = d

print(furthest)
