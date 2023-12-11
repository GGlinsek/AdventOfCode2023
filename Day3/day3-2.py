f = open("day3", "r")

numbers = ["1","2","3","4","5","6","7","8","9","0"]
symbols = ["!","#","$","%","&","/","(",")","=","?","*","@", "+"]
coordinatessymbols = []
coordinatesnumbers = {}
sum = 0
x = 0
counter = 0
starsymbols = {}
for line in f.readlines():
    line = line.strip("\n")
    y=0
    test = 0
    for i in range(0,len(line)):
        if test == i:
            asdas = line[i]
            if line[i] != "." and line[i] not in numbers:
                if line[i] == "*":
                    starsymbols[(x,i)] = ["1"]
                else:
                    coordinatessymbols.append((x,i))

            elif line[i] in numbers:
                if line[i+2] in numbers and line[i+1] in numbers:
                    coordinatesnumbers[line[i:i+3], counter] = ((x,i),3)
                    test+=2
                    counter+=1
                elif line[i+1] in numbers:
                    coordinatesnumbers[line[i:i + 2], counter] = ((x, i), 2)
                    test += 1
                    counter += 1
                else:
                    coordinatesnumbers[line[i], counter] = ((x, i), 1)
                    counter += 1
            test += 1


    x+=1

for (number,counter),((x,y),length) in coordinatesnumbers.items():
    flag = True
    if (x,y-1) in starsymbols.keys():
        starsymbols[(x,y-1)].append(number)
    elif (x,y+length) in starsymbols.keys():
        starsymbols[(x,y+length)].append(number)
    elif (x,y-1) in coordinatessymbols or (x,y+length) in coordinatessymbols:
        flag = False
    for i in range(-1,length+1):
        if (x-1,y+i) in starsymbols.keys():
            starsymbols[(x-1,y+i)].append(number)
        elif (x+1,y+i) in starsymbols.keys():
            starsymbols[(x+1,y+i)].append(number)
        elif (x-1,y+i) in coordinatessymbols or (x+1,y+i) in coordinatessymbols:
            flag = False

    if not flag:
        #sum += int(number)
        print(number)

for item in starsymbols.values():
    print(item)
    if len(item) > 2:
        sum += int(item[len(item)-1]) * int(item[len(item)-2])

print(coordinatesnumbers)
print(coordinatessymbols)
print(sum)