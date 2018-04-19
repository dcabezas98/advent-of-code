from string import ascii_uppercase

diagram = []

with open("input.txt") as f:
    for line in f:
        diagram.append(list(line[:-1]))

def turn(i,j,direction):
    if direction != 'u':
        if i < len(diagram)-1 and (diagram[i+1][j] in ascii_uppercase or diagram[i+1][j] == '|'):
            return 'd'

    if direction != 'd':
        if diagram[i-1][j] in ascii_uppercase or diagram[i-1][j] == '|':
            return 'u'

    if direction != 'r':
        if j > 0 and (diagram[i][j-1] in ascii_uppercase or diagram[i][j-1] == '-'):
            return 'l'

    return 'r'
        
letters = []
i = 0
j = diagram[0].index('|')
direction = 'd'

while diagram[i][j] != ' ':
    if direction == 'd':
        i += 1

    elif direction == 'u':
        i -= 1

    elif direction == 'r':
        j += 1

    else: #elif direction == 'l':
        j -= 1

    if diagram[i][j] in ascii_uppercase:
        letters.append(diagram[i][j])

    elif diagram[i][j] == '+':
        direction = turn(i,j,direction)
        
print(''.join(letters))
