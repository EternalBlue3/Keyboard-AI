import itertools, time, sys

with open("Test.txt", "r") as fh:
    test = ''.join(fh.readlines()).replace('\n', '').replace(' ', '').lower()
    fh.close()

keyboard = "qwertyuiopasdfghjkl;zxcvbnm,.?"
keyboard = [keyboard[:10],
            keyboard[10:20],
            keyboard[20:30]
            ]

fingers = [[1, 0], [1, 1], [1, 2], [1, 3], [1, 6], [1, 7], [1, 8], [1, 9]] # Y, X
distance = 0

for x in keyboard:
    print(x)
print()

for letter in test:
    for y, row in enumerate(keyboard):
        if letter in row:
            x = row.index(letter)
            
            if x < 3 or x > 6: # Are we NOT dealing with keys in the middle
                
                fingery = fingers[x][0] if x <= 3 else fingers[x-2][0] # Get finger from list
                difference = abs(y - fingery) # Get y value difference

                if y == 0 and fingery == 1 or y == 1 and fingery == 0:  # From y=1 to y=0 or y=0 to y=1 (distance += 1.032)
                    distance += 1.032

                elif y == 2 and fingery == 1 or y == 1 and fingery == 2:  # From y=1 to y=2 or y=2 to y=1 (distance += 1.118)
                    distance += 1.118
                    
                elif difference == 2:
                    distance += 2.138
                    
                if x <= 3:
                    fingers[x][0] = y
                else:
                    fingers[x-2][0] = y
                    
                print(letter, round(distance,6))
            
            else: # x == 3, 4, 5 or 6 (need to use fingers to access middle keys) (we HAVE to deal with middle keys)
                
                fingery, fingerx = fingers[3] if x == 4 or x == 3 else fingers[4] # Get correct finger for the middle keys
                movement = (fingerx-x, fingery-y) # Get the movement to get to the keys
                
                if movement == (-1,0) or movement == (1,0): # If the finger moves to the side by one (distance += 1)
                    distance += 1
                    
                elif movement == (0,1): # Movement == Up one
                    if fingery == 1:
                        distance += 1.032
                    elif fingery == 2:
                        distance += 1.118
                elif movement == (0,-1): # Movement == Down one
                    if fingery == 0:
                        distance += 1.032
                    if fingery == 1:
                        distance += 1.118
                    
                elif movement == (-1,1): # Movement == Up one, right one (distance += 1.247 or 1.118)
                    if fingery == 1:
                        distance += 1.247
                    elif fingery == 2:
                        distance += 1.118
                elif movement == (1,-1): # Movement == Down one, left one (distance += 1.247 or 1.118)
                    if fingery == 0:
                        distance += 1.247
                    elif fingery == 1:
                        distance += 1.118
                    
                elif movement == (1,1): # Movement == Up one, left one (distance += 1.605 or 1.803)
                    if fingery == 1:
                        distance += 1.605
                    elif fingery == 2:
                        distance += 1.803
                elif movement == (-1,-1): # Movement == Down one, right one (distance += 1.605 or 1.803)
                    if fingery == 0:
                        distance += 1.605
                    elif fingery == 1:
                        distance += 1.803
                
                elif movement == (-1,2) or movement == (1,-2): # Movement == Up two, right one or down two, left one (distance += 2.015)
                    distance += 2.015
                    
                elif movement == (1,2) or movement == (-1,-2): # Movement == Up two, left one or down two, right one (distance += 2.661)
                    distance += 2.661
                    
                elif movement == (0,2) or movement == (0,-2): # Movement == Up two, x doesn't change (distance += 2.138)
                    distance += 2.138
                    
                elif movement == (0,0): # No movement == no distance
                    pass
                    
                else: # Print out movement error if error occurs
                    print("Error: ",movement)
                    sys.exit(1)
                    
                if x == 3 or x == 4:
                    fingers[3][0] = y
                    fingers[3][1] = x
                else:
                    fingers[4][0] = y
                    fingers[4][1] = x
                    
                print(movement, letter, round(distance,6))
                
            distance = round(distance, 6)

print("Total distance: ", distance)
