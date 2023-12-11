f = open("day4", "r")

sum = 0
for line in f.readlines():
    line = line.split(":")[1].split("|")
    winning = line[0].strip().split()
    actual = line[1].strip().split()
    cardsum = 0.5
    for number in actual:
        if number in winning:
            cardsum *= 2
    if cardsum > 0.5:
        sum += cardsum

print(sum)