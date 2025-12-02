import re

theFile = open("AdventOfCode2025/dayTwo.txt","r")
fileLine = theFile.readline()
theLines = fileLine.split(",")
total = 0
found = []

pattern = r'^\d+${2}'

for line in theLines:
    theVals = line.split("-")
    for i in range(int(theVals[0]), int(theVals[1])+1):
        if len(str(i)) % 2 == 0:
            mid = len(str(i)) // 2 + len(str(i)) % 2
            if str(i)[:mid] == str(i)[mid:]:
                total += i
                found.append(i)
                
print(total)
#print(found)

foundVals = []
totalVal = 0
pattern = r'^\d+${2}'

for line in theLines:
    theVals = line.split("-")
    for i in range(int(theVals[0]), int(theVals[1])+1):
        if re.fullmatch(r"(.+)\1+", str(i)):
            totalVal += i
            foundVals.append(i)
          
print(totalVal)
#print(foundVals)