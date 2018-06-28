
pattern = [['.','#','.'],['.','.','#'],['#','#','#']]

rules_book_inputs = {}
rules_book_outputs = {}

with open("input.txt") as f:
    for line in f:
        i, o = line[:-1].split(" => ")
        i = i.split("/")
        i = list(map(list,i))
        o = o.split("/")
        o = list(map(list,o))

        rules_book = {}
