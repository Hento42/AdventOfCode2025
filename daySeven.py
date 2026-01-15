from functools import cache

theFile = open("daySeven.txt","r")
fileLines = theFile.readlines()
total = 0
lineNum = 0
tachyons = []

# Part 1

ind = 0
for char in fileLines[0]:
    if char == "S":
        tachyons.append(ind)
    ind += 1

while lineNum < len(fileLines) -1:
    newTachyons = []
    lineNum += 1
    for i in range(len(fileLines[lineNum])):
        if fileLines[lineNum][i] == "^" and i in tachyons:
            if (i-1) not in newTachyons or (i+1) not in newTachyons:
                newTachyons.append(i - 1)
                newTachyons.append(i + 1)
                total += 1
            tachyons.remove(i)
    if newTachyons != []:
        newTachyons = list(set(newTachyons))
        for tach in newTachyons:
            tachyons.append(tach)
        tachyons = list(set(tachyons))

print(total)


# Part 2

timelines = 0
start = []
manifold = [[char for char in line.strip()] for line in fileLines]

ind = 0
for char in manifold[0]:
    if char == "S":
        start = (0,ind)
    ind += 1

@cache
def getTimes(pos):
    if pos[0] == len(manifold) - 1:
        return 1
    elif manifold[pos[0] + 1][pos[1]] == ".":
        return getTimes((pos[0] + 1, pos[1]))
    elif manifold[pos[0] + 1][pos[1]] == "^":
        return (getTimes((pos[0] + 1, pos[1] - 1)) + getTimes((pos[0] + 1, pos[1] + 1)))

print(getTimes(start))