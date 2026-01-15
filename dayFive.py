theFile = open("dayFive.txt","r")
fileLines = theFile.readlines()
theInts = []
nums = []
total = 0

for line in fileLines:
    if line.__contains__("-"):
        theInts.append(line.strip("\n").split("-"))
    elif line.strip("\n") != "":
        nums.append(int(line.strip("\n")))

print(theInts)

# Part 1

for num in nums:
    fresh = False
    for ints in theInts:
        if num >= int(ints[0]) and num <= int(ints[1]):
            fresh = True
    
    if fresh:
        total += 1

print(total)


# Part 2

count = 0
usedRanges = []

def range_subset(range1, range2):
    if not range1 or not range2 or (len(range1) > 1 and range1.step % range2.step):
        return False
    return range1.start in range2 and range1[-1] in range2


for ints in theInts:
    low = int(ints[0])
    high = int(ints[1])
    change = True
    
    while change:
        change = False
        for vals in usedRanges:
            if low in range(int(vals[0]), int(vals[1]) + 1) and (low <= int(ints[1])):
                low = int(vals[1]) + 1
                change = True
            if high in range(int(vals[0]), int(vals[1]) + 1) and (high >= int(ints[0])):
                high = int(vals[0]) - 1
                change = True
    for i in usedRanges:
        if range_subset(range(int(i[0]), int(i[1])), range(low, high)):
            count -= (int(i[1]) - int(i[0]) + 1)
    if (high - low) >= 0:
        count += (high - low + 1)
    usedRanges.append(ints)

print(count)
