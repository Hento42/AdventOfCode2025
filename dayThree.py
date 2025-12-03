theFile = open("AdventOfCode2025/dayThree.txt","r")
fileLines = theFile.readlines()
total = 0

for line in fileLines:
    line = line.strip("\n")
        
    max = 0
    maxInd = -1
    
    for i in range(len(line)-1):
        if int(line[i]) > max:
            max = int(line[i])
            maxInd = i
            
    maxTwo = 0
    twoInd = -1
            
    for j in range(maxInd+1, len(line)):
        if int(line[j]) > maxTwo:
            maxTwo = int(line[j])
            twoInd = j
            
    num = int(str(max) + str(maxTwo))
    
    total += num
print(total)


total = 0

for line in fileLines:
    line = line.strip("\n")
    theNum = ""
        
    maxs = [0 for x in range(13)]
    maxInds = [-1 for x in range(13)]
    
    for val in range(12,0,-1):
        
        for i in range(maxInds[val]+1,len(line)-(val-1)):
            if int(line[i]) > maxs[val-1]:
                maxs[val-1] = int(line[i])
                maxInds[val-1] = i
                
    maxs = maxs[0:-1]
    maxInds = maxInds[0:-1]
    maxs.reverse()
    maxInds.reverse()
    
    for num in maxs:
        theNum += str(num)
        
    total += int(theNum)

print(total)


            