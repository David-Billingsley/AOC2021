prevdepth = 0
numofincress = 0

with open('depth.txt') as f:
    for depth in f.readlines():
        if int(prevdepth) == 0:
            prevdepth = int(depth)
        elif int(prevdepth) < int(depth):
            numofincress += 1
            prevdepth = int(depth)

print(numofincress)
