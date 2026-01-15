import math

theFile = open("dayEight.txt","r")
fileLines = theFile.readlines()
juncBoxes = []
dist = {}
circuits = []

for line in fileLines:
    juncBoxes.append(tuple(map(int, line.strip("\n").split(","))))

for box in juncBoxes:
    for junc in juncBoxes:
        if box != junc and (box, junc) not in dist.keys() and (junc, box) not in dist.keys():
            dist[(box, junc)] = math.dist(box, junc)

ordered = {key: value for key, value in sorted(dist.items(), key=lambda item: item[1])}
# Part 1

for i in range(10):
    found = False
    circuits.append(list(ordered.keys())[i])

conns = []
changed = True
while changed:
    changed = False
    for circuit in circuits:
        found = False
        ind = 0
        for con in conns:
            if (any(i in circuit for i in con)) and not found:
                conns[ind] += (circuit)
                found = True
                changed = True
            else:
                ind += 1
        if not found:
            conns.append(circuit)
    if changed:
        circuits = conns
        conns = []


counts = []

for con in conns:
    count = 0
    used = []
    for tup in con:
        if tup not in used:
            count += 1
            used.append(tup)
    counts.append(count)

print((sorted(counts))[-1] * (sorted(counts))[-2] * (sorted(counts))[-3])


# Part 2

circuits = []
lastTwo = []
conns = []
index = 0
counts = []


while count < len(fileLines) or len(circuits) > 1:
    circuits.append(list(ordered.keys())[index])
    lastTwo = list(ordered.keys())[index]
    for circuit in circuits:
        found = False
        ind = 0
        for con in conns:
            if (any(i in circuit for i in con)) and not found:
                conns[ind] += (circuit)
                found = True
            else:
                ind += 1
        if not found:
            conns.append(circuit)
    circuits = conns
    used = []
    count = 0
    for tup in conns[0]:
        if tup not in used:
            count += 1
            used.append(tup)
    conns = []
    index += 1

print(lastTwo[0][0] * lastTwo[1][0])