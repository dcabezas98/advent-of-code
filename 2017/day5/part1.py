
jumps = 0

pos = 0

end = False

with open("input.txt") as f:

    maze = f.read().split('\n')
    
    l = len(maze)
    
    maze = maze[:l-1]

    l -= 1

    maze = list(map(int,maze))

    while not end:

        maze[pos] +=1
        pos += maze[pos]-1

        jumps +=1
        
        if pos >= l:
            end = True

    print(jumps)
