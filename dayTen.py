import itertools

theFile = open("dayTen.txt","r")
fileLines = theFile.readlines()
total = 0

# Part One

def toggle(lights, button):
    for ind in button:
        if lights[ind] == ".":
            lights[ind] = "#"
        elif lights[ind] == "#":
            lights[ind] = "."
    return lights

def getFewestPresses(buttons, theLights):
    for i in range(1,len(theLights)):
        for p in (list(itertools.permutations(buttons, i))):
            current = ["." for x in range(len(theLights))]
            for b in p:
                current = toggle(current,b)
                if current == theLights:
                    return i

for line in fileLines:
    theLights = []
    buttons = []

    theLights = list(line.split("]")[0].strip("["))
    buttons = (line.split("]")[1].split("{")[0].split())
    ind = 0

    for button in buttons:
        buttons[ind] = eval(button)
        if type(buttons[ind]) == int:
            buttons[ind] = (buttons[ind], )
        ind += 1

    total += getFewestPresses(buttons, theLights)

print(total)


# Part Two

total = 0

def increment(joltage, button):
    for ind in button:
        joltage[ind] += 1
    return joltage

def getFewest(buttons, joltages):
    current = [0 for x in range(len(joltages))]
    print(current)
                

for line in fileLines:
    buttons = []
    joltages = []

    buttons = (line.split("]")[1].split("{")[0].split())
    joltages = list(map(int,(line.split("{")[1].strip("}\n").split(","))))
    print(joltages)

    ind = 0
    for button in buttons:
        buttons[ind] = eval(button)
        if type(buttons[ind]) == int:
            buttons[ind] = (buttons[ind], )
        ind += 1
    print(buttons)

    getFewest(buttons, joltages)


print(total)
