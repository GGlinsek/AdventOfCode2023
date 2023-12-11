f = open("day3", "r")

numbers = ["1","2","3","4","5","6","7","8","9","0"]
symbols = ["!","#","$","%","&","/","(",")","=","?","*","@", "+"]
coordinatessymbols = []
coordinatesnumbers = {}
sum = 0
x = 0
counter = 0
for line in f.readlines():
    line = line.strip("\n")
    y=0
    test = 0
    for i in range(0,len(line)):
        if test == i:
            asdas = line[i]
            if line[i] != "." and line[i] not in numbers:
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
    if (x,y-1) in coordinatessymbols or (x,y+length) in coordinatessymbols:
        flag = False
    for i in range(-1,length+1):
        if (x-1,y+i) in coordinatessymbols or (x+1,y+i) in coordinatessymbols:
            flag = False

    if not flag:
        sum += int(number)
        print(number)



print(coordinatesnumbers)
print(coordinatessymbols)
print(sum)