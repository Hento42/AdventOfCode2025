import matplotlib.pyplot as plt


theFile = open("dayNine.txt","r")
fileLines = theFile.readlines()
redSquares = []
areas = {}

for line in fileLines:
    redSquares.append(tuple(map(int, line.strip("\n").split(","))))

# Part 1

for sq1 in redSquares:
    for sq2 in redSquares:
        if sq1 != sq2 and (sq1, sq2) not in areas.keys() and (sq2, sq1) not in areas.keys():
            areas[(sq1, sq2)] = ((abs(sq1[0] - sq2[0])+1) * (abs(sq1[1] - sq2[1])+1))
        

ordered = {key: value for key, value in sorted(areas.items(), key=lambda item: item[1])}
print(ordered[list(ordered)[-1]])


# Part 2 - incomplete

x = [coord[0] for coord in redSquares]
y = [coord[1] for coord in redSquares]
areas = {}


plt.plot(x,y,"o-")
plt.show()
rightInd = -1

for ind in range(len(x)-1):
    if x[ind] < 10000 and x[ind+1] > 90000:
        rightInd = ind
        break

# Above

rightCoord = (x[rightInd+1], y[rightInd+1])
maxY = 0

for ind in range(len(x)-1):
    if x[ind] > rightCoord[0] and x[ind+1] < rightCoord[0]:
        maxY = y[ind]
        break


for sq1 in redSquares:
    if sq1 != rightCoord and (sq1, rightCoord) not in areas.keys() and (rightCoord, sq1) not in areas.keys() and sq1[1] > 50000 and sq1[1] < maxY:
        valid = True
        index = redSquares.index(sq1)
        for i in range(index, rightInd-1):
            if redSquares[i][0] > sq1[0] and redSquares[i][1] < sq1[1]:
                valid = False
        if valid:
            areas[(sq1, rightCoord)] = ((abs(sq1[0] - rightCoord[0])+1) * (abs(sq1[1] - rightCoord[1])+1))


# Below

rightCoord = (x[rightInd+2], y[rightInd+2])
minY = 0

for ind in range(len(x)-1):
    if x[ind] < rightCoord[0] and x[ind+1] > rightCoord[0]:
        minY = y[ind]
        break


for sq1 in redSquares:
    if sq1 != rightCoord and (sq1, rightCoord) not in areas.keys() and (rightCoord, sq1) not in areas.keys() and sq1[1] < 50000 and sq1[1] > minY:
        valid = True
        index = redSquares.index(sq1)
        for i in range(rightInd-1, index):
            if redSquares[i][0] > sq1[0] and redSquares[i][1] > sq1[1]:
                valid = False
        if valid:
            areas[(sq1, rightCoord)] = ((abs(sq1[0] - rightCoord[0])+1) * (abs(sq1[1] - rightCoord[1])+1))


ordered = {key: value for key, value in sorted(areas.items(), key=lambda item: item[1])}
print(ordered[list(ordered)[-1]])
