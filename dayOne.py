theFile = open("AdventOfCode2025/dayOne.txt","r")
fileLines = theFile.readlines()
theVal = 50
zeroCount = 0
count = 0

for line in fileLines:
    op = str(line[0])
    num = int(line[1:])
    val = 0
            
    if op == "R":
        val = 1
    elif op == "L":
        val = -1
        
    for i in range(num):
        theVal += val
        theVal = theVal % 100
        if theVal == 0:
            count += 1
            
    if theVal == 0:
        zeroCount += 1
    
    
print(theVal, zeroCount, count)


