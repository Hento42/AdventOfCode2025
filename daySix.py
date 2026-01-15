theFile = open("daySix.txt","r")
fileLines = theFile.readlines()
total = 0
theNums = []

for line in fileLines:
    theNums.append(line.strip("\n").split())

# Part 1

rotated = list(zip(*theNums[::-1]))

for calc in rotated:
    value = 0

    if calc[0] == "*":
        value = 1
        for ind in range(1,len(calc)):
            value *= int(calc[ind])

    elif calc[0] == "+":
        value = 0
        for ind in range(1,len(calc)):
            value += int(calc[ind])

    total += value

print(total)



# Part 2

total = 0
maxLength = 0
theLines = []
splitVals = []

spaces = 0
for item in fileLines[-1].strip("\n"):
    if item != " ":
        splitVals.append(spaces)
        spaces = 0
    else:
        spaces += 1
splitVals.append(spaces+1)
splitVals = splitVals[1:]

index = 0

for line in fileLines:
    line = line.strip("\n")
    i = 0
    index = 0
    tempLine = []
    while i < len(line):
        tempLine.append(line[i:i+splitVals[index]])
        i += splitVals[index] + 1
        index += 1
    theLines.append(tempLine)
    

flipped = list(zip(*list(zip(*list(zip(*theLines[::-1]))[::-1]))[::-1]))


for calc in flipped:
    value = 0
    
    maxLength = len(calc[-1])
    values = ["" for x in range(maxLength)]

    for count in range(maxLength-1, -1, -1):
        for ind in range(len(calc)-1):
            if calc[ind][count] != " ":
                values[count] += calc[ind][count]

    values = list(map(int, values))


    if calc[-1].strip() == "*":
        value = 1
        
        for val in values:
            value *= val

    elif calc[-1].strip() == "+":
        value = 0

        for val in values:
            value += val

    total += value
print(total)
