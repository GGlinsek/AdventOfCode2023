f = open("day4", "r")

def rekurz(linenumber, winninglines):
    sum = 0
    for i in range(0,winninglines):
        sum+=1
        line = lines[linenumber+i].split(":")[1].split("|")
        winning = line[0].strip().split()
        actual = line[1].strip().split()
        cardsum = 0
        for number in actual:
            if number in winning:
                cardsum += 1
        if cardsum > 0:
            sum += rekurz(linenumber+i+1, cardsum)
    return sum




sum = 0
lines = []
for line in f.readlines():
    lines.append(line.strip())

print(lines)


for i in range(0,len(lines)):
    sum += rekurz(i, 1)
print(sum)



