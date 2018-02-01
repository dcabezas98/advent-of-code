
target = 361527

seq = [1, 1, 2, 4, 5, 10, 11, 23, 25]

square = 3 # Square of the spiral
e = 0 # Element inside that square

# The square m has 8*(m-1) elements (except square 1)
# The lenght of the side of square m is 2m-1
# The vertices of the square m are the elements 2m-3, 4m-5, 6m-7 and 8m-9

while seq[-1] <= target:

    n = seq[-1]
    
    if e == 0: # Element is the element immediately after the last vertex
        n += seq[len(seq)-8*(square-2)]

    elif e == 1: 
        n += seq[-2]
        n += seq[len(seq)-8*(square-2)]
        n += seq[len(seq)-8*(square-2)-1]

    elif e > 1 and e <= 2*square-3: # Element in the right side
        n += seq[len(seq)-8*(square-2)-2]

        if e < 2*square-3: # Element is not the first vertex
            n += seq[len(seq)-8*(square-2)-1]

        if e < 2*square-4: # Element is not the element immediately before the first vertex
            n += seq[len(seq)-8*(square-2)]

    elif e == 2*square-2: # Element is the element immediately after the first vertex
        n += seq[-2]
        n += seq[len(seq)-8*(square-2)-2]
        n += seq[len(seq)-8*(square-2)-3]

    elif e > 2*square-2 and e <= 4*square-5: # Element in the top side
        n += seq[len(seq)-8*(square-2)-4]

        if e < 4*square-5: # Element is not the second vertex
            n += seq[len(seq)-8*(square-2)-3]

        if e < 4*square-6: # Element is not the element immediately before the second vertex
            n += seq[len(seq)-8*(square-2)-2]

    elif e == 4*square-4: # Element is the element immediately after the second vertex
        n += seq[-2]
        n += seq[len(seq)-8*(square-2)-4]
        n += seq[len(seq)-8*(square-2)-5]
        
    elif e > 4*square-4 and e <= 6*square-7: # Element in the left side
        n += seq[len(seq)-8*(square-2)-6]
        
        if e < 6*square-7: # Element is not the third vertex
            n += seq[len(seq)-8*(square-2)-5]

        if e < 6*square-8: # Element is not the element immediately before the third vertex
            n += seq[len(seq)-8*(square-2)-4]

    elif e == 6*square-6: # Element is the element immediately after the third vertex
        n += seq[-2]
        n += seq[len(seq)-8*(square-2)-6]
        n += seq[len(seq)-8*(square-2)-7]

    elif e > 6*square-6 and e <= 8*square-9: # Element in the bottom side
        n += seq[len(seq)-8*(square-2)-8]
        n += seq[len(seq)-8*(square-2)-7]
        
        if e < 8*square-9: # Element is not the fourth vertex   
            n += seq[len(seq)-8*(square-2)-6]
        
    seq.append(n)
    e += 1

    if e == 8*(square-1):
        e = 0
        square += 1

print(seq)
