theFile = open("dayFour.txt","r")
fileLines = theFile.readlines()
total = 0
theArray = []

for line in fileLines:
    tempArray = []
    line = line.strip("\n")
    for item in line:
        tempArray.append(item)
    theArray.append(tempArray)
    
dirs = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
print(theArray)

# Part 1

for i in range(len(theArray)):
    for j in range(len(theArray)):
        if theArray[i][j] == "@":
            adj = 0

            for dir in dirs:
                if ((i + dir[0]) in range(len(theArray)) and (j + dir[1]) in range(len(theArray)) and theArray[(i + dir[0])][(j + dir[1])] == "@"):
                    adj += 1
        
            if adj < 4:
                total += 1

print(total)


# Part 2

changed = 1
total = 0

while changed > 0:
    changed = 0

    for i in range(len(theArray)):
        for j in range(len(theArray)):
            if theArray[i][j] == "@":
                adj = 0

                for dir in dirs:
                    if ((i + dir[0]) in range(len(theArray)) and (j + dir[1]) in range(len(theArray)) and theArray[(i + dir[0])][(j + dir[1])] == "@"):
                        adj += 1
            
                if adj < 4:
                    total += 1
                    changed += 1
                    theArray[i][j] = "."


print(total)

            