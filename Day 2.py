depth = 0
direction = 0

with open('movements.txt') as f:
    for movement in f.readlines():
        if "up" in movement:
            depth = depth - int(movement[2:])
        elif "down" in movement:
            depth = depth + int(movement[4:])
        elif "forward" in movement:
            direction = direction + int(movement[7:])
        elif "backwords" in movement:
            direction = direction + int(movement[9:])

print(f'Toal depth = {direction * depth}')
