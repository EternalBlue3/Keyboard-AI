def evaluate(keyboard, test):
    distance = 0  # Total distance
    last_used = 0  # Last finger used
    fingers = [[1, 0], [1, 1], [1, 2], [1, 3], [1, 6], [1, 7], [1, 8], [1, 9]]  # Y, X
    static_fingers = [finger[:] for finger in fingers]  # Create a copy of static_fingers

    for letter in test:
        if letter == ' ':
            fingers = [finger[:] for finger in static_fingers]
            continue
        for y, row in enumerate(keyboard):
            if letter in row:
                x = row.index(letter)

                if x != last_used:
                    if last_used <= 3:
                        fingers[last_used] = static_fingers[last_used][:]
                    elif last_used == 3 or last_used == 4:
                        fingers[3] = static_fingers[3][:]
                    elif last_used == 5 or last_used == 6:
                        fingers[4] = static_fingers[4][:]
                    else:
                        fingers[last_used - 2] = static_fingers[last_used - 2][:]
                last_used = x

                if x < 3 or x > 6:  # Are we NOT dealing with keys in the middle
                    finger = fingers[x] if x <= 3 else fingers[x - 2]  # Get finger from list
                    fingery = finger[0]
                    difference = abs(y - fingery)  # Get y value difference

                    if (y == 0 and fingery == 1) or (y == 1 and fingery == 0):  # From y=1 to y=0 or y=0 to y=1 (distance += 1.032)
                        distance += 1.032
                    elif (y == 2 and fingery == 1) or (y == 1 and fingery == 2):  # From y=1 to y=2 or y=2 to y=1 (distance += 1.118)
                        distance += 1.118
                    elif difference == 2:
                        distance += 2.138

                    if x <= 3:
                        fingers[x][0] = y
                    else:
                        fingers[x - 2][0] = y
                else:  # x == 3, 4, 5 or 6 (need to use fingers to access middle keys) (we HAVE to deal with middle keys)
                    finger = fingers[3] if x == 4 or x == 3 else fingers[4]  # Get correct finger for the middle keys
                    fingery, fingerx = finger
                    movement = (fingerx - x, fingery - y)  # Get the movement to get to the keys

                    if movement == (-1, 0) or movement == (1, 0):  # If the finger moves to the side by one (distance += 1)
                        distance += 1
                    elif movement == (0, 1):  # Movement == Up one
                        distance += 1.032 if fingery == 1 else 1.118
                    elif movement == (0, -1):  # Movement == Down one
                        distance += 1.032 if fingery == 0 else 1.118
                    elif movement == (-1, 1):  # Movement == Up one, right one (distance += 1.247 or 1.118)
                        distance += 1.247 if fingery == 1 else 1.118
                    elif movement == (1, -1):  # Movement == Down one, left one (distance += 1.247 or 1.118)
                        distance += 1.247 if fingery == 0 else 1.118
                    elif movement == (1, 1):  # Movement == Up one, left one (distance += 1.605 or 1.803)
                        distance += 1.605 if fingery == 1 else 1.803
                    elif movement == (-1, -1):  # Movement == Down one, right one (distance += 1.605 or 1.803)
                        distance += 1.605 if fingery == 0 else 1.803
                    elif movement == (-1, 2) or movement == (1, -2):  # Movement == Up two, right one or down two, left one (distance += 2.015)
                        distance += 2.015
                    elif movement == (1, 2) or movement == (-1, -2):  # Movement == Up two, left one or down two, right one (distance += 2.661)
                        distance += 2.661
                    elif movement == (0, 2) or movement == (0, -2):  # Movement == Up two, x doesn't change (distance += 2.138)
                        distance += 2.138

                    if x == 3 or x == 4:
                        fingers[3][0] = y
                        fingers[3][1] = x
                    else:
                        fingers[4][0] = y
                        fingers[4][1] = x

        distance = round(distance, 6) # Round because floating point math is broken in python

    return distance
